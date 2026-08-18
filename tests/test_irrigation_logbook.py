import importlib.util,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('x',Path(__file__).parents[1]/'src/irrigation_logbook.py');x=importlib.util.module_from_spec(s);s.loader.exec_module(x)
class T(unittest.TestCase):
 def test_domain_workflow(self):
  r=x.run([{'zone':'A','minutes':30,'liters_per_minute':4}],'2026-08-18',7); self.assertTrue(r[0]['liters']==120)
if __name__=='__main__':unittest.main()
