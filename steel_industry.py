
import bchain2 as b


class mines:
  def __init__(self, productionDetails, index):
      self.productionDetails = productionDetails
      self.index = index
      self.block = b.Block(productionDetails,index, "NA", "NA")

class Trader:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)

class smelterStorage:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)

class Furnance:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)

class steelMaking:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)

class secondaryProcess:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)

class Transporter:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)

class Manufacturers:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)

class Sales:
  def __init__(self, data, index, prev_index, prev_hash):
      self.data = data
      self.index = index
      self.prev_index = prev_index
      self.prev_hash = prev_hash
      self.block = b.Block(data,index,prev_index, prev_hash)




mineA = mines("production = 1000 tn", 1)
mineB = mines("production = 5000 tn", 2)
trader1 = Trader("500 Tn", 3, 1, mineA.block.hash())
trader2 = Trader("500 Tn", 4, 1, mineA.block.hash())
trader3 = Trader("2000 Tn", 5, 2, mineB.block.hash())
trader4 = Trader("3000 Tn", 6, 2, mineB.block.hash())
smelter1 = smelterStorage("2000 Tn", 7, 5, trader3.block.hash())
smelter2 = smelterStorage("3000 Tn", 8, 6, trader4.block.hash())
furnance = Furnance("3000 Tn consumption 2000 Tn output ", 9, 8, smelter2.block.hash())
steelmaking = steelMaking("1000 Tn", 10, 9, furnance.block.hash())
secondaryprocess = secondaryProcess("800 Tn", 11, 10, steelmaking.block.hash())
transporter = Transporter("700 Tn", 12, 11, secondaryprocess.block.hash())
manufacturer = Manufacturers("600 Tn", 13, 12, transporter.block.hash())
sales = Sales("600 Tn", 14, 13, manufacturer.block.hash())

print(mineA.productionDetails)
print(mineA.block.hash())

print(mineB.productionDetails)
print(mineB.block.hash())

print(trader1.data)
print(trader1.block.hash())
print(trader1.prev_hash)

print(trader2.data)
print(trader2.block.hash())
print(trader2.prev_hash)

print(trader3.data)
print(trader3.block.hash())
print(trader3.prev_hash)

print(trader4.data)
print(trader4.block.hash())
print(trader4.prev_hash)

print(smelter1.data)
print(smelter1.block.hash())
print(smelter1.prev_hash)

print(smelter2.data)
print(smelter2.block.hash())
print(smelter2.prev_hash)

print(furnance.data)
print(furnance.block.hash())
print(furnance.prev_hash)

print(steelmaking.data)
print(steelmaking.block.hash())
print(steelmaking.prev_hash)

print(secondaryprocess.data)
print(secondaryprocess.block.hash())
print(secondaryprocess.prev_hash)

print(transporter.data)
print(transporter.block.hash())
print(transporter.prev_hash)

print(manufacturer.data)
print(manufacturer.block.hash())
print(manufacturer.prev_hash)

print(sales.data)
print(sales.block.hash())
print(sales.prev_hash)