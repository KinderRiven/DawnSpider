#encoding=utf-8
from Athena.Akame_ga_KILL.Tatsumi import Tatsumi
from Athena.Akame_ga_KILL.Mine import Mine


mine = Mine()

urls = mine.load_list()
#urls = ["http://dm1080p.com/archives/4531"]
dm = Tatsumi(mine, max_run=3, debug=0, lazy=2, start_mission=500)
dm.import_urls(urls)

#print "Mission Start."
dm.start()
#print "Mission Running."
dm.join()
#print "Mission End."