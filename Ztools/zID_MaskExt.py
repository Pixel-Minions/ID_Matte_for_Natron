def inputChanged(inputIndex, thisNode, thisGroup, app):
	thisNode.get_Res.setExpression("thisNode.getInput(0).getRegionOfDefinition(0.0,0).width()", False, 0)
	thisNode.get_Res.setExpression("thisNode.getInput(0).getRegionOfDefinition(0.0,0).height()", False, 1)
	
	
	
def createInstanceExt(app,group):
	#Note that the callback belongs to the PyPlug to so we use it as prefix 
	group.onInputChanged.set("zID_Mask.inputChanged")	
	