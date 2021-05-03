#Define a class Complex which represents the complex number. And overload + 
#operator which add two complex objects.

class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img
    self.eq = str(real)+" + "+str(img)+"i"
    
  def __add__(self, one):
    real = self.real + one.real
    img = self.img + one.img
    return Complex(real,img)
    
nums1 = [int(x) for x in input("Enter space separated real & imaginary for first eq: ").split()]
nums2 = [int(x) for x in input("Enter space separated real & imaginary for second eq: ").split()]
a = Complex(nums1[0], nums1[1])
b = Complex(nums2[0], nums2[1])
c = a + b

print("("+a.eq+") + ("+b.eq+") =",c.eq)