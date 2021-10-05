import math

def is_perfect_square(nr):
    '''
    Determina daca un numar este patrat perfect.
    :param x:int
    :return:True, daca numarul este patrat perfect, False , daca numarul nu este patrat perfect.
    '''
    if math.sqrt(nr)==int(math.sqrt(nr)):
        return True
    else:
        return False



def get_perfect_squares(a,b):
    '''
    Afiseaza toate patratele perfecte dintr-un interval inchis dat
    :param a:int
    :param b:int
    :return:lista
    '''
    list=[]
    for i in range(a,b+1):
        if is_perfect_square(i)==True:
            list.append(i)
    return list



def test_get_perfect_squares():
    assert is_perfect_square(4) is True
    assert is_perfect_square(9) is True
    assert is_perfect_square(7) is False
    assert is_perfect_square(27) is False

def is_leap_years(an):
    '''

    :param an: int
    :return: int
    '''
    if an%400==0 or an%4==0 and an%100!=0 :
        return True
    else:
        return False

def get_leap_years(an1,an2) :
    '''

    :param an1: int
    :param an2: int
    :return: list
    '''

    list2=[]
    for j in range(an1+1,an2) :
        if is_leap_years(j)==True :
            list2.append(j)
    return list2

def test_get_leap_years() :
    assert is_leap_years(1604) is True
    assert is_leap_years(1600) is True
    assert is_leap_years(1872) is True
    assert is_leap_years(1601) is False



if __name__=="__main__":
    test_get_perfect_squares()
    test_get_leap_years()
    while True:
      print("1.Afiseaza toate patratele perfecte dintr-un interval inchis dat: ")
      print("2.Afiseaza toti anii bisecti intre doi an dati: ")
      print("x.Iesire")
      optiune=input("Alege optiune: ")

      if optiune == '1' :
          nr1=int(input("Dati primul numar: "))
          nr2=int(input("Dati al doilea numar: "))
          retlist=get_perfect_squares(nr1,nr2)
          print(retlist)
      elif optiune=='2' :
          an1=int(input("Dati primul an: "))
          an2=int(input("Dati al doilea an: "))
          if an1>an2 :
            an1,an2=an2,an1
          retlist2=get_leap_years(an1,an2)
          print(retlist2)
      else:
          break



