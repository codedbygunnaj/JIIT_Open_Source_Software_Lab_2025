def countAvg(lis):
    avg=sum(lis)/len(lis)
    return


Perfect 👍 you’ve locked on to the functional version:

def count_above_average(nums):
    avg = sum(nums) / len(nums)
    return len(list(filter(lambda x: x > avg, nums)))


Let’s break this down in a teaching mode (slow + step by step):

🔹 Step 1: What is filter?

filter(function, iterable)

It tests each element of the iterable with the function.

If the function returns True, the element is kept.

If it returns False, the element is discarded.

It gives back a filter object (like a lazy list), so we usually wrap it in list() to see the result.

👉 Example:

nums = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # [2, 4]

🔹 Step 2: What is lambda?

lambda creates a small anonymous function (function without a name).

Syntax:

lambda arguments: expression


lambda x: x > avg means → take x, return True if x > avg.

👉 Example:

f = lambda x: x*2
print(f(5))  # 10

🔹 Step 3: Applying to your function
filter(lambda x: x > avg, nums)


For each number x in nums, check if x > avg.

Keeps only the numbers above average.

Example:

nums = [10, 20, 30, 40]
avg = 25
filter(lambda x: x > 25, [10,20,30,40]) → [30, 40]

🔹 Step 4: Wrapping with list() and len()

list(filter(...)) → turns filter object into a list.

len(...) → counts how many numbers were above average.

So finally:

return len(list(filter(lambda x: x > avg, nums)))


means:
👉 “Count how many numbers in nums are above the average.” ✅

🎯 Formula used:

avg = sum(nums) / len(nums)

sum(nums) → adds all numbers.

len(nums) → counts total numbers.

Division gives the mean (average).


# iterable yani list pass ki one by onme function mei and agar true hua to add hoga list mei warna nahi hoga