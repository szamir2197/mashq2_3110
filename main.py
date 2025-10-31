class Kompyuter:
    def __init__(self, model, ram, disk_hajmi):
        self.model = model
        self.ram = ram
        self.disk_hajmi = disk_hajmi

    def malumot(self):
        """Kompyuter ma'lumotlarini qaytaradi"""
        return f"Model: {self.model}, RAM: {self.ram} GB, Disk hajmi: {self.disk_hajmi} GB"

    def ram_yangila(self, yangi_ram):
        """RAMni yangilaydi"""
        self.ram = yangi_ram
        return f"RAM yangilandi. Yangi RAM: {self.ram} GB"


komp1 = Kompyuter("Dell Inspiron", 8, 512)

print(komp1.malumot())   
print(komp1.ram_yangila(16))    
print(komp1.malumot())         
