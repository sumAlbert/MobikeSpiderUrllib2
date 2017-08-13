# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for num in xrange(105):
        print ('thread.start_new_thread(link,('+str(50*num)+','+str(50*num+50)+'))')