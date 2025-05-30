class TagCloud:
    def __init__(self, tags=None):
        if tags is None:
            tags = []
        self.tags = tags

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def get_tags(self):
        return self.tags

    def __str__(self):
        return ', '.join(self.tags) # Return a string of all tags
    
    
    def __len__(self):
        return len(self.tags) # Return the number of tags in the cloud
    def __contains__(self, tag):
        return tag in self.tags
    def __iter__(self):
        return iter(self.tags)
    def __getitem__(self, index):
        return self.tags[index] if 0 <= index < len(self.tags) else None        
    def __setitem__(self, index, tag):
        if 0 <= index < len(self.tags):
            self.tags[index] = tag
        else:
            raise IndexError("Index out of range")
    def __delitem__(self, index):
        if 0 <= index < len(self.tags):
            del self.tags[index]
        else:
            raise IndexError("Index out of range")
    def __eq__(self, other):
        if isinstance(other, TagCloud):
            return self.tags == other.tags
        return False
    def __ne__(self, other):
        if isinstance(other, TagCloud):
            return self.tags != other.tags
        return True
    def __lt__(self, other):
        if isinstance(other, TagCloud):
            return len(self.tags) < len(other.tags)
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, TagCloud):
            return len(self.tags) <= len(other.tags)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, TagCloud):
            return len(self.tags) > len(other.tags)
        return NotImplemented   
    def __ge__(self, other):
        if isinstance(other, TagCloud):
            return len(self.tags) >= len(other.tags)
        return NotImplemented
    def __hash__(self):
        return hash(tuple(self.tags))
    def __repr__(self):
        return f"TagCloud({self.tags})"
    def __bool__(self):
        return bool(self.tags)
    def clear(self):
        self.tags.clear()
    def copy(self):
        return TagCloud(self.tags.copy())
    def extend(self, tags):
        self.tags.extend(tags)
    def index(self, tag):
        return self.tags.index(tag)
    def count(self, tag):
        return self.tags.count(tag)
    def sort(self, reverse=False):
        self.tags.sort(reverse=reverse)
    def reverse(self):
        self.tags.reverse()
    def to_list(self):
        return self.tags.copy()
    def from_list(self, tags):
        self.tags = tags.copy() if isinstance(tags, list) else []
    def __add__(self, other):
        if isinstance(other, TagCloud):
            return TagCloud(self.tags + other.tags)
        return NotImplemented
    
