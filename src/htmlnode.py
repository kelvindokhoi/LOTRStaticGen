class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is not None:
            return ''.join(f' {key}="{value}"' for key,value in self.props.items())
        return ''
    
    def __repr__(self):
        return f"TAG: {self.tag}\nVALUE: {self.value}\nCHILDREN: {self.children}\nPROPS: {self.props}"
    
    def __eq__(self, other):
        return self.tag==other.tag and self.value==other.value and self.children==other.children and self.props==other.props
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)
    
    def to_html(self):
        if self.value is None and self.props is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value if self.value is not None else''}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
        return f"<{self.tag}>{"".join(child.to_html() for child in self.children)}</{self.tag}>"
    