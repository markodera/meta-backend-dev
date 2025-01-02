class Payslips:
    def __init__(self, name, payment, amount) -> None:    
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not payed yet"
        
mark = Payslips("Mark", "no", 1000)
bash = Payslips("Bash", "no", 3000)
print(mark.status(),"\n",bash.status())


bash.pay()
print("After payment")
print(mark.status(),"\n",bash.status())