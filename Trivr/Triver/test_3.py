# -*- coding: utf-8 -*-


def main():
    """
    Add Documentation here
    """
    a = '<1> <2> <3> <4> <5> <6> '
    print(a)
    a = a.replace(' ', '')
    print(a)
    a = a.replace('<','')
    print(a)
    a = a.split('>')
    print(a)
    a.pop()
    print(a)
    print(len(a))
    # """
    # with open('test.txt','r') as file_handle:
    #     env = file_handle.read()
    # print('1: ' + env+ '\n')
    # env = env.replace(' ', '')
    # print('2: ' + env+ '\n')
    # env = env.replace('\n','')
    # print('3: ' + env + '\n')
    # #print(env)
    # """

if __name__ == '__main__':
    main()