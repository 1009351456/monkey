import os
import shutil
import random

class Corpus: 
    def __init__(self, name, percent=50):
        self.name = name
        self.cd = os.path.dirname(os.path.realpath(__file__))
        self.imagedir = os.path.join(self.cd, "data")
        self.newimagedir = os.path.join(self.name, "data")    
        self.celldir = os.path.join(self.name, "cell") 
                
        # Create and rework paths.
        
        if os.path.isdir(self.newimagedir):
            shutil.rmtree(self.newimagedir)
        os.makedirs(self.newimagedir)            

        if os.path.isdir(self.celldir):
            shutil.rmtree(self.celldir)
        os.makedirs(self.celldir)
    
        for root, dirs, files in os.walk(self.imagedir):
            for subdir in dirs:
                os.makedirs(os.path.join(self.newimagedir, subdir))
                
        # Now add the images.

        self.images = []
        self.unused = {} 
        self.subdirs = []
        for subdir in os.listdir(self.imagedir):
            self.subdirs.append(subdir)
            fullpath = os.path.join(self.imagedir, subdir)
            self.images = os.listdir(fullpath)
            self.unused[subdir] = os.listdir(fullpath)    
            for i in range(0, int(len(self.images)*percent/100.0)):
                image = random.choice(self.images)
                self.images.remove(image)
                self.unused[subdir].remove(image)
                filepath = os.path.join(self.imagedir, subdir, image) 
                target = os.path.join(self.newimagedir, subdir)
                shutil.copy(filepath, target)    
                
        print(self.newimagedir)

    def get_corpus(self):
        return self.newimagedir

    def get_next_images(self, name=None, count=2): 
        self.empty_cell()
        if name is None:
            name = random.choice(self.subdirs)
        fullpath = os.path.join(self.celldir, name)
        os.makedirs(fullpath)
        for n in xrange(count):
            item = random.choice(self.unused[name])
            self.unused[name].remove(item)
            fullpath = os.path.join(self.imagedir, name, item)
            target = os.path.join(self.celldir, name)
            shutil.copy(fullpath, target)

        return fullpath    
   
    def empty_cell(self):
        try:
            shutil.rmtree(self.celldir)
        except Exception:
            pass
        
        os.makedirs(self.celldir)
