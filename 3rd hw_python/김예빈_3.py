# key : value
profile = {"이름" : "김멋사"}


key = input("key값을 입력해주세요 :")
value = input("value값을 입력해주세요 :")

profile.update({key:value})
print(profile)

