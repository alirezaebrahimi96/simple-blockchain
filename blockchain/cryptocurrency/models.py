from django.db import models
from .utils import create_new_ref_number
from unixtimestampfield.fields import UnixTimeStampField
# Create your models here.



class Node(models.Model):
    address = models.CharField(default=create_new_ref_number, unique=True, max_length=32)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return f"Id:{self.id}, Wallet:{self.wallet}"

class Transaction(models.Model):
    id = models.IntegerField(default=create_new_ref_number, unique=True, primary_key=True)
    sender = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="sender")
    reciption = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="reciption")
    amount = models.IntegerField()

    def __str__(self):
        return f"Sender:{self.sender.address}, Reciption:{self.reciption.address}, Amount:{self.amount}"


class Blockchain(models.Model):
    index = models.IntegerField(default=create_new_ref_number, unique=True, primary_key=True)
    timestamp = UnixTimeStampField(auto_now_add=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    proof = models.IntegerField()
    previous_hash = models.IntegerField()

    def __str__(self):
        return f"Index:{self.index}, Transaction:{self.transaction.id}, Timestamp:{self.timestamp}"
