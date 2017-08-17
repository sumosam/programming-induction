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
  if (len(arr) < 2):
    return False
  return partition_helper(arr, len(arr)-1, target)



#partition_helper: ArrayOf(Natural), ArrayIndex, Natural -> Boolean
#Purpose: find out if array can be partitioned to equal a particular number. 
#This will be done by seeing if we should "take the last element"

#Stub:
#def partition_helper(arr, i, target):
#  return False

def partition_helper(arr, i, target):
  if (target == 0):
    return True
  elif (i < 0 and target > 0):
    return False
  else:
    return partition_helper(arr, i-1, target-arr[i]) or partition_helper(arr, i-1, target)



#Examples and Tests:
class TestSuite(unittest.TestCase):
  def test_canPartition(self):
    self.assertEqual(canPartition([1,5,11,5]), True)
    self.assertEqual(canPartition([1,5,3]) , False)
    self.assertEqual(canParition([1]), False)
    self.assertEqual(canPartition([0,1]), False)
    self.assertEqual(canPartition([1,1]), True)
    self.assertEqual(canPartition([11, 3, 7, 1, 0, 5, 9, 2, 2]), True)

  def test_partition_helper(self):
    self.assertEqual(partition_helper([1,5,11,5],3, 11), True)
    self.assertEqual(partition_helper([1,5,11], 2, 8.5), False)
    self.assertEqual(partition_helper([2,3,3,4], 3, 6), True)






if __name__ == '__main__':
  unittest.main()