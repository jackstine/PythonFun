from random import random

def need_to_begin(investment):
	what_needs=[]
	needs=[]
	Finished=False
	catch=''
	quit=True
	while quit:
		try:
			print "type [Q] if you want to quit"
			catch=raw_input("Please type in a investment that needs another to be completed. ")
			if catch=='q' or catch=='Q':
				quit=False
				break	
			catch=int(catch)-1
			what_needs+=[catch]
			for index in range(len(investment)):
				if what_needs[len(what_needs)-1]==index:
					needs+=[input("Please type in the investment that the previous question needs")-1]
					in_it=True
			if in_it:	
				in_it=False
				for index in range(len(investment)):
					if needs[len(needs)-1]==index:
						in_it=True
				if in_it:	
					Finished=True
			elif type(())==type(5):
				hey=1
		except:
			print "Please enter valid answers"
			if Finished==False:
				if len(what_needs)>1:
					what_needs=what_needs[:len(what_needs)-1]
				elif len(what_needs)==1:
					what_needs=[]
					
	return what_needs,needs


def budget_constraint():
	budget=0
	while True:
		try: 
			budget= input("Please type in a budget contraint! ")
			return budget
		except: print "that is not valid, must be integer"


def mutually_exclusive_constraints(investment):
	muts=[]
	print "type [Q] to not enter"
	while True:
		
		try:
			value=raw_input("enter mutually exclusive variable position (from the order in which you entered in the investments. ")
			if value=='q' or value=='Q':
				print muts
				return muts 
			value=int(value)-1
			for index in range(len(investment)):
				if value==index:
					print value
					muts+=[value]
					print muts
			print "that is not in the range of investments!!!!!"
		except:
			print"must enter a integer"

def first_input(info):
	while True:
		try: 
			info+=[input("insert only a number please. ")]
			return info
		except: print"input must be a integer"

def correct_input(info,string,quit):
	your_input=''
	while quit:
		try:
			if string=="insert the next investment. ":
				print "type [Q] to quit"
			your_input=raw_input(string)
			if string== "insert the next investment. "and (your_input=='q' or your_input=='Q'):
				quit=False
				return info,quit
			else:
				your_input=int(your_input)
				info+=[your_input]
				return info,quit
		except:print"input must be a integer"
	return info,quit

def create_decisions(investment,pw):
	print "press Q to quit inserting investments!!!"
	quit=True
	First=True
	invest_string="insert the next investment. "
	pw_string="insert the next present worth. "
	try:
		investment+=[input("insert the first investment. ")]
	except:
		investment+=first_input(investment)
	try:
		pw+=[input("insert the first present worth. ")]
	except:
		pw+=first_input(pw)
		First=False
	while quit:
		investment,quit=correct_input(investment,invest_string,quit)
		pw,quit=correct_input(pw,pw_string,quit)
	return investment,pw

def calc_max_pw(accept,max_pw,max_pw_accept,budget):#calc the max_pw and following accepted track
	cost=0
	total_pw=0
	for index,value in enumerate(accept):
		if value==1:
			cost+=investment[index]
			total_pw+=pw[index]
	if cost<=budget and max_pw<total_pw:
		max_pw=total_pw
		max_pw_accept=accept[:]
		return max_pw_accept,max_pw
	return max_pw_accept,max_pw


def unless_con(accept,what_needs,needs):#returns true if unless contraints are followed
	for index_what in what_needs:
		if accept[index_what]==1:
			for index_needs in needs:
				if accept[index_needs]==0:
					return False
	return True


def mutually_exclusive(accept,mut_variable):#returns true if mut_ex flase otherwise
	mut1=[]
	mut2=[]
	for mut_index in mut_variable:
		for mut_index2 in mut_variable:
			if (accept[mut_index]==1 and accept[mut_index2]==1)and mut_index!=mut_index2:
				return False
	return True


def create_accepted(accept_token):
	for i in range(len(investment)):
		accept_token+=[0]
	return accept_token

def banken(accept,bank,bank_left):#iterates through all already accepted lists
	add_to_bank=True
	if len(bank)==0:
		bank+=[accept[:]]
		bank_left=False
		add_to_bank=False
	else:
		for index in bank:
			if accept==index:
				bank_left=True
				add_to_bank=False	
				break
		if add_to_bank==True:
			bank+=[accept[:]]
			bank_left=False
	return accept,bank,bank_left

def create_random(accept,bank):#creates the accept and sees if it has been use yet
	bank_left=True
	while bank_left:
		for i in range(len(investment)):
			accept[i]=int(round(random()))
		accept,bank,bank_left=banken(accept,bank,bank_left)
	return accept,bank

#list of all variables
bank=[]
accept=[]
investment=[]
pw=[]
iteration=0
accepted_max=0
total_pw=0
max_pw=0
max_pw_accept=[]
mut_ex=False
unless_statement=False
mut_variable=[]
budget=0
what_needs=[]
needs=[]

#program starts now***********************************8
investment,pw=create_decisions(investment,pw)

accept=create_accepted(accept)

max_pw_accept=create_accepted(max_pw_accept)

budget=budget_constraint()

mut_variable=mutually_exclusive_constraints(investment)

what_needs,needs=need_to_begin(investment)

max_bank=2**len(investment)


while iteration<max_bank:
	accept,bank=create_random(accept,bank)

	mut_ex=mutually_exclusive(accept,mut_variable)

	if mut_ex:	
		unless_statement=unless_con(accept,what_needs,needs)

		if unless_statement:
			max_pw_accept,max_pw=calc_max_pw(accept,max_pw,max_pw_accept,budget)		
	iteration+=1

print "accept these choices ",max_pw_accept 
print "this is the max present worth ",max_pw
