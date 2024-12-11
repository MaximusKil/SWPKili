class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Worker(Person):
    def __init__(self, name, gender, branch = None):
        super().__init__(name, gender)
        self.branch = branch

    def set_branch(self, branch):
        if self.branch is not None:
            raise ValueError(f"Mitarbeiter {self.name} ist bereits in einer Abteilung zugeordnet.")
        self.branch = branch
        branch.add_worker(self)

    def __str__(self):
        branch_name = self.branch.name if self.branch else "Keine Abteilung"
        return f"{super().__str__()}, Abteilung: {branch_name}"

class Branchmanager(Worker):
    def __init__(self, name, gender, branch):
        super().__init__(name, gender)
        self.branch = branch
        branch.set_branchmanager(self)

    def __str__(self):
        return f"{super().__str__()} (Abteilungsleiter)"

class Branch:
    def __init__(self, name):
        self.name = name
        self.worker = []
        self.branchmanager = None

    def add_worker(self, worker):
        if worker not in self.worker:
            self.worker.append(worker)

    def set_branchmanager(self, branchmanager):
        if self.branchmanager is not None:
            raise ValueError(f"Abteilung {self.name} hat bereits einen Abteilungsleiter: {self.branchmanager.name}")
        self.branchmanager = branchmanager
        self.add_worker(branchmanager)

    def __str__(self):
        worker_namen = ", ".join([m.name for m in self.worker])
        manager_name = self.branchmanager.name if self.branchmanager else "Keiner"
        return f"Abteilung: {self.name}, Abteilungsleiter: {manager_name}, Mitarbeiter: [{manager_name}]"

    def workercount(self):
        return len(self.worker)

class Firma:
    def __init__(self, name):
        self.name = name
        self.branch = []

    def add_branch(self, branch):
        if branch not in self.branch:
            self.branch.append(branch)

    def count_worker(self):
        return sum(len(branch.worker) for branch in self.branch)

    def count_branchmanager(self):
        return sum(1 for branch in self.branch if branch.branchmanager is not None)

    def count_branch(self):
        return len(self.branch)

    def biggest_branch(self):
        return max(self.branch, key=lambda abt: abt.workercount(), default=None)

    def prozent_gender(self):
        all_worker = [worker for branch in self.branch for worker in branch.worker]
        count_all = len(all_worker)
        there = count_all > 0
        count_f = sum(1 for worker in all_worker if worker.gender == "f")
        count_m = count_all - count_f
        f_prozent = (count_f / count_all) * 100 if there else 0
        m_prozent = (count_m / count_all) * 100 if there else 0
        return f_prozent, m_prozent

    def __str__(self):
        branch_info = "\n".join([str(branch) for branch in self.branch])
        return f"Firma: {self.name}\n{branch_info}"

if __name__ == "__main__":
    firma = Firma("Kili GmbH")

    it_branch = Branch("IT")
    hr_branch = Branch("HR")
    firma.add_branch(it_branch)
    firma.add_branch(hr_branch)

    worker1 = Worker("Alice", "f")
    worker2 = Worker("Bob", "m")

    worker1.set_branch(it_branch)
    worker2.set_branch(hr_branch)

    manager_it = Branchmanager("Charlie", "m", it_branch)

    print(firma)
    print(f"Anzahl Mitarbeiter: {firma.count_worker()}")
    print(f"Anzahl Abteilungsleiter: {firma.count_branchmanager()}")
    print(f"Anzahl Abteilungen: {firma.count_branch()}")
    biggest_branch = firma.biggest_branch()
    if biggest_branch:
        print(f"Größte Abteilung: {biggest_branch.name} mit {biggest_branch.workercount()} Mitarbeitern")
    f_prozent, m_prozent = firma.prozent_gender()
    print(f"Prozentanteil Frauen: {f_prozent:.2f}%, Männer: {m_prozent:.2f}%")
