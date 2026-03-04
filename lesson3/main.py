class Message:
    def process(self):
        pass

class TextMessage(Message):
    def process(self):
        print('processing text msg')

class ImageMessage(Message):
    def process(self):
        print('process img msg')

txt = TextMessage()
img = ImageMessage()

# txt.process()
# img.process()

def process_msg(message: Message):
    print(message.process())

messages = [TextMessage(), ImageMessage()]

# for msg in messages:
#     process_msg(msg)


class DataSet:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        combined = self.data + other.data
        return DataSet(combined)
    
    def __str__(self):
        return f'DataSet: {self.data}'
    

d1 = DataSet([1,2,3])
d2 = DataSet([4,5,6])

combined_data = d1 + d2
# print(combined_data)


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
   def process_payment(self, amount):
       print(f"Processing credit card payment of {amount} USD.")

class PayPalProcessor(PaymentProcessor):
   def process_payment(self, amount):
       print(f"Processing PayPal payment of {amount} USD.")