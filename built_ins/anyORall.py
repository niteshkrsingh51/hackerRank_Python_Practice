def any_all_palindromic(number_list):
  if all(int(i) >= 0 for i in number_list):
      if any(num == num[-1:] for num in number_list):
          print(True)
      else:
          print(False)
  else:
      print(False)


numberCount = int(input())
number_list = [(number_list) for number_list in input().split(" ")]
any_all_palindromic(number_list)
