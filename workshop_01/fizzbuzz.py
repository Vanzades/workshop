# requirement:
# 1. buat function dengan nama "get_fizzbuzz"
# 2. function tersebut menerima 1 input tipe number
# 3. apabila input habis dibagi 3 return "fizz"
# 4. apabila input habis dibagi 5 return "buzz"
# 5. apabila input habis dibagi 3 dan 5 return "fizz_buzz"
# 6. selain itu, return sesuai input

class FizzBuzz:

    def getFizzBuzz(input):
        
        if input % 15 == 0:
            return "fizz_buzz"
        elif input % 3 == 0:
            return "fizz"
        elif input % 5 == 0:
            return "buzz"
        else:
            return input