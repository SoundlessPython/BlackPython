amount = int(input('Enter number: '))
if amount<1000:
   discount = amount*0.10
   print("Discount",discount)

else:
  discount = amount*0.15
  print("Discount",discount)

print("Net payable",amount-discount)
