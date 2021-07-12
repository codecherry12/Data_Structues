'''https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
Now modify print_tree method to take tree level as input. And that should print tree only upto that level as shown below
Global
   |__India
      |__Gujarat
      |__Karnataka
   |__USA
      |__New Jersey
      |__Californi
'''
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self,level):
        if self.get_level()>level:
            return
        spaces=' '*self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_Location_tree():
    globe=TreeNode("Global")

    gujarat=TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka=TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    Newjersey=TreeNode("New Jersey")
    Newjersey.add_child(TreeNode("Princeton"))
    Newjersey.add_child(TreeNode("Trenton"))

    California=TreeNode("California")
    California.add_child(TreeNode("San Francisco"))
    California.add_child(TreeNode("Mountain View"))
    California.add_child(TreeNode("Palo Alto"))

    India=TreeNode("India")
    India.add_child(gujarat)
    India.add_child(karnataka)

    USA=TreeNode("USA")
    USA.add_child(Newjersey)
    USA.add_child(California)

    globe.add_child(India)
    globe.add_child(USA)

    return globe
if __name__=="__main__":
    root=build_Location_tree()
    root.print_tree(2)
