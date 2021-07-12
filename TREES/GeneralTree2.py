"""https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
Nilpul
   |__Chinmay
      |__Vishwa
         |__Dhaval
         |__Abhijit
      |__Aamir
   |__Gels
      |__Peter
      |__Waqas
Tree with only designation

CEO
   |__CTO
      |__Infrastructure Head
         |__Cloud Manager
         |__App Manager
      |__Application Head
   |__HR Head
      |__Recruitment Manager
      |__Policy Manager
Tree with both name and designation

Nilpul(CEO)
   |__Chinmay(CTO)
      |__Vishwa(Infrastructure Head)
         |__Dhaval(Cloud Manager)
         |__Abhijit(App Manager)
      |__Aamir(Application Head)
   |__Gels(HR Head)
      |__Peter(Recruitment Manager)
      |__Waqas(Policy Manager)
"""
class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
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

    def print_tree(self,property_name):
        if property_name=='both':
            value= self.name +"("+self.designation+")"
        elif property_name=='name':
            value=self.name
        else:
            value=self.designation
        spaces=' '*self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

def Build_management_tree():
    #CEO Hierarchy
    ceo=TreeNode("Nilpul","CEO")

    #CTO Hierarchy
    infra_head=TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit","App Manager"))

    cto=TreeNode("Chinmay","CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir","Application Head"))

    #HR Hierarchy
    hr_head=TreeNode("Gels","HR Head")
    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas","Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__=="__main__":
    root_node=Build_management_tree()
    print("Tree with only name")
    print()
    root_node.print_tree("name")
    print("Tree with only designation")
    print()
    root_node.print_tree("designation")
    print("Tree with both name and designation")
    print()
    root_node.print_tree("both")
