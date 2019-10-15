import os
import pandas

committees = ['C00646844','C00545616','C00699660','C00648725','C00650507','C00708875','C00710103','C00693630','C00648915','C00704064','C00703843','C00706457','C00711457','C00658633','C00716589','C00652248','C00694778','C00652719','C00696872','C00703736','C00657361','C00693556','C00482307','C00708412','C00649376','C00703504','C00706747','C00706564','C00697144','C00705327','C00704429','C00704379','C00698795','C00694216','C00705343','C00711713','C00648956','C00499392','C00633859','C00715631','C00637074','C00706267','C00653816','C00713958','C00648220','C00664375','C00672295','C00708289','C00633362','C00694265','C00707612','C00650150','C00649913','C00704643','C00714204','C00715482','C00666149','C00655571','C00717306','C00661868','C00715466','C00590810','C00521948','C00649483','C00607416','C00607416','C00713693','C00710749','C00714865','C00701706','C00700583','C00588558','C00702225','C00662874','C00510164','C00710533','C00637868','C00699579','C00713933','C00715235','C00648493','C00712794','C00575209','C00719039','C00670034','C00714089','C00717876','C00721027','C00640045','C00701003','C00703199','C00652297','C00705079','C00655613','C00711945','C00717322','C00656686','C00703058','C00694653','C00711572','C00660464','C00253187','C00610071','C00717959','C00633982','C00704981','C00638650','C00476291','C00712265','C00707430','C00709519','C00700757','C00704270','C00656785','C00710962','C00711317','C00575167','C00639310','C00698779','C00371203','C00301838','C00710459','C00635342','C00711630','C00471946','C00499236','C00700922','C00707521','C00433524','C00715029','C00721332','C00635888','C00556365','C00702191','C00655183','C00701227','C00373563','C00693663','C00694208','C00694687','C00650622','C00495846','C00509968','C00650648','C00665638','C00639146','C00681544','C00706333','C00634212','C00701102','C00701946','C00312017','C00651042','C00657411','C00582890','C00694091','C00716050','C00657155','C00636571','C00698670','C00700807','C00700559','C00706051','C00640003','C00701250','C00662650','C00717405','C00467571','C00500207','C00709881','C00664797','C00711887','C00717330','C00614776','C00660795','C00696146','C00472704','C00660472','C00272211','C00706549','C00392688','C00698134','C00707026','C00662668','C00662767','C00713297','C00650697','C00200584','C00701599','C00552547','C00701334','C00711564','C00371302','C00709006','C00405431','C00636670']

df = pandas.read_csv('data/source/filings.csv')

compete = df[df['committee_id'].isin(committees)]

# only_competitive

q3 = compete[compete['report_type']=='Q3']

files = list(q3['file_number'])

print(files)