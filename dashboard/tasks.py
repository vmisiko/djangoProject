import random
import string
from celery import shared_task
from .models import WithdrawPayouts, Conversion, AccountsModel
from Home.models import Order
from djangoProject.mpesa.b2c import b2c_payments
from . payout import paypal_payout_release
from django.utils import timezone

sender_batch_id =''.join(
    random.choice(string.ascii_uppercase) for i in range(12)
        
    )

@shared_task
def mpesa_payout_task(pk_model):

    queryset = WithdrawPayouts.objects.filter(pk__in = pk_model)
    print("Celery worker now working")
    if queryset:
        print("qs available")
        qs = queryset.filter(status=False, payment_mode="M")
        
        for q in qs:
            phone_number = str(q.phone_number)
            amount1 = q.amount
            phone = phone_number.split("+")[1]

            # convert to kES
            conversion = Conversion.objects.all()
            rate = [con.rate for con in conversion][0]
            amount = int(amount1)* int(rate)

            print(phone)
            # b2c_payments(amount,phone)
            try:
                b2c_payments(amount,phone)
                q.status= True
                q.save()
            except:
                pass

    else:
        print("qs not available")
        
@shared_task
def paypal_payout_task(pk_model):

    queryset = WithdrawPayouts.objects.filter(pk__in = pk_model)
    print("Celery worker now working")
    if queryset:

        qs = queryset.filter(status=False, payment_mode="p")
        

        items = [ ]
       
        for q in qs:       
            payout = {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": q.amount,
                    "currency": "USD"
                },
                "receiver": q.email,
                "note": "congratulations and thank you for working with freelancing Accounts, keep up the spirit.",
                "sender_item_id": sender_batch_id,
            }
            items.append(payout)

        qs.update(status = True)

        paypal_payout_release(items)


@shared_task
def release_payment():
    # accounts = AccountsModel.objects.all()
    orders = Order.objects.filter(ordered=True, released=False, refund= False)
    d1 = timezone.now()
    for order in orders:
        print("worker order releasing")
        d2 =order.ordered_date

        amount = order.get_total()

        buyer = order.user


        seller = order.seller

        print(f" buyer and seller: {buyer} - {seller}")

        account_buyer = AccountsModel.objects.get(user__username= buyer)
        

        if abs(d1-d2).days >=3:
            amount1 = int(account_buyer.amount) - int(amount)

            order.released = True

            order.save()
            print(F'{amount1}, is the buyers balance from {account_buyer.amount}')
            account_buyer.amount = int(amount1)

            account_buyer.save()
            
            seller_account = AccountsModel.objects.get(user__username = seller)
            amount2 = seller_account.amount
            amount_deduct = int(amount) - 2
            print(amount, amount_deduct, "this is deducted amounts")
            amount3 = int(amount2) + int(amount_deduct)

            seller_account.amount = amount3

            seller_account.save()
            
        else:

            print(" three days still not yet completed")





