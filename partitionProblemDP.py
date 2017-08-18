import unittest
#The partition problem

#Can a given set of numbers be partitioned into 
#two subsets such that the sum of elements in both subsets
#are the same. 

#Examples given:
# arr = [1, 5, 11, 5]
# output: true

# arr = [1, 5, 3]
# output: false


#canPartition: ArrayOf(Natural) -> Boolean
#Invariants: Natural >=0
#Purpose: produce true if the set of numbers can be partitioned 
#into two subsets that have the same sum. 
#Produce false otherwise. 

#stub
#def canPartition(arr):
#  return False


def canPartition(arr):
  #find the target of the array for each subset
  total = sum(arr)
  target = total/2
  if (target % 1) != 0:
    return False
  if (len(arr) < 2):
    return False
  return partition_helper(arr, int(target))



#partition_helper: ArrayOf(Natural), ArrayIndex, Natural -> Boolean
#Purpose: find out if array can be partitioned to equal a particular number. 
#This will be done by seeing if we should "take the last element"

#Stub:
#def partition_helper(arr, target):
#  return False

def partition_helper(arr, target):
  dpTable = [[None for x in range(len(arr)+1)] for y in range(target+1)]
  #where target = 0, dpTable[:][0] = True
  for j in range(len(arr)+1):
    dpTable[0][j] = True
  #where target >0 AND out of array
  for i in range(1,target+1):
    dpTable[i][0] = False
  #where target >0 and within array
  for i in range(1,target+1):
    for j in range(1,len(arr)+1):
      if (i - arr[j-1]) < 0:
        dpTable[i][j] = dpTable[i][j-1] 
      else:
        dpTable[i][j] = dpTable[i -arr[j-1]][j-1] or dpTable[i][j-1] 

  return dpTable[target][len(arr)]



#Examples and Tests:
class TestSuite(unittest.TestCase):
  def test_canPartition(self):
    self.assertEqual(canPartition([1,5,11,5]), True)
    self.assertEqual(canPartition([1,5,3]) , False)
    self.assertEqual(canPartition([1]), False)
    self.assertEqual(canPartition([0,1]), False)
    self.assertEqual(canPartition([1,1]), True)
    self.assertEqual(canPartition([11, 3, 7, 1, 0, 5, 9, 2, 2]), True)

  def test_partition_helper(self):
    self.assertEqual(partition_helper([1,5,11,5], 11), True)
    #our partition helper no longer deals with incoming fractions
    #self.assertEqual(partition_helper([1,5,11], 8.5), False)
    self.assertEqual(partition_helper([2,3,3,4], 6), True)



if __name__ == '__main__':
  unittest.main()