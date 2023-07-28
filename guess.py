import random
class Tebak:
  def __init__(self):
    self.start = int(input("Mau dari berapa? "))
    self.limit = int(input("Mau sampai berapa? "))
    self.jawaban = random.randint(self.start, self.limit)
    self.tebakan = 0
    self.tries = 0
    
  def cek(self):
    if self.tebakan == self.jawaban:
      return True
    return False
  
  def cekPositif(self):
    if self.jawaban > 0:
      print("Jawabannya bilangan positif")
    else:
      print("Jawabannya bilangan negatif")
  
  def cekGenap(self):
    if self.jawaban % 2 == 0:
      print("Jawabannya angka genap")
    else:
      print("Jawabannya angka ganjil")
  
  def cekBesar(self, previous):
    if self.jawaban > previous:
      print("Jawabannya lebih besar")
    else:
      print("Jawabannya lebih kecil")
  
  
  def main(self):
    self.tebakan = int(input("Tebak angka {0} sampai {1}: ".format(self.start, self.limit)))
    if self.cek():
      print("Jawaban Anda BENAR!!")
    else:
      print("Jawaban Anda SALAH!!")
      self.tries += 1
      if self.tries == 1:
        if self.start < 0:
          self.cekPositif()
        else:
          self.tries += 1
          self.cekGenap()
      elif self.tries == 2:
        self.cekGenap()
      else:
        self.cekBesar(self.tebakan)
      self.main()