#explaining global and non local 
def scope_test():
    def do_local():
    	var1="local_variable"
    def scope_nonlocal():
    	nonlocal var1
    	var1="nonlocalvariable"
    def scope_global():
        global var1
        var1="globallydefinedvariable"
    var1= "testing"
    do_local()
    print ("after local assignment: ",var1)
#will print testing overriding local variable defined above"

    scope_nonlocal()
    print ("after non local assignment: ",var1)
# will print "nonlocalvariable" variable non local variables don't change values inside functions
    scope_global()
    print ("after global assignment: ",var1)
# will print "nonlocalvariable" variable non local variables don't change values inside functions

scope_test()
print ("In global scope:" , var1)

# will print ""globallydefinedvariable" variable non local variables don't change values inside functions
