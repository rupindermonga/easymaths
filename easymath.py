


from operator import add, sub
from random import choice, randint

ops = {'+' : add, '-' : sub}
MaxTries = 2

def doprob():
        op = choice('+-')
        nums = [randint(1,10) for i in range(2)]
        nums.sort(reverse = True)
        ans = ops[op](*nums)
        pr = '%d %s %d = ' % (nums[0], op, nums[1])
        oops = 0
        while True:
            try:
                if int(input(pr)) == ans:
                    print("correct")
                    break
                if oops == MaxTries:
                    print("Answer\n%s%d"%(pr, ans))
                else:
                    print("incorrect... try again")
                    oops += 1
            except (KeyboardInterrupt, EOFError, ValueError):
                print("Invalid input... try again")

def main():
    while True:
        doprob()
        try:
            opt = input("Again? [y]").lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()