to_lnglat_dict = {
    '经度': 'lng',
    '纬度': 'lat',
    'lon': 'lng',
    'lng_WGS': 'lng',
    'lat_WGS': 'lat',
    'lon_WGS': 'lng',
    'longitude': 'lng',
    'latitude': 'lat',
    'geom': 'geometry'}

UTIL_CN_NUM = {'〇': '0',
               '零': '0',
               '一': '1',
               '二': '2',
               '两': '2',
               '三': '3',
               '四': '4',
               '五': '5',
               '六': '6',
               '七': '7',
               '八': '8',
               '九': '9'}

epsg_dict = {
    '阿克苏地区': 32644,
    '阿拉尔市': 32644,
    '阿拉善盟': 32648,
    '阿勒泰地区': 32645,
    '阿里地区': 32644,
    '安康市': 32649,
    '安庆市': 32650,
    '安顺市': 32648,
    '安阳市': 32650,
    '鞍山市': 32651,
    '巴彦淖尔市': 32648,
    '巴中市': 32648,
    '白城市': 32651,
    '白山市': 32652,
    '白银市': 32648,
    '百色市': 32648,
    '蚌埠市': 32650,
    '包头市': 32649,
    '宝鸡市': 32648,
    '保定市': 32650,
    '保山市': 32647,
    '北海市': 32649,
    '北京市': 32650,
    '北屯市': 32645,
    '本溪市': 32651,
    '毕节市': 32648,
    '滨州市': 32650,
    '亳州市': 32650,
    '沧州市': 32650,
    '昌都市': 32647,
    '常德市': 32649,
    '常州市': 32650,
    '朝阳市': 32651,
    '潮州市': 32650,
    '郴州市': 32649,
    '成都市': 32648,
    '承德市': 32650,
    '澄迈县': 32649,
    '池州市': 32650,
    '赤峰市': 32650,
    '崇左市': 32648,
    '滁州市': 32650,
    '达州市': 32648,
    '大连市': 32651,
    '大庆市': 32651,
    '大同市': 32649,
    '大兴安岭地区': 32651,
    '丹东市': 32651,
    '儋州市': 32649,
    '德阳市': 32648,
    '德州市': 32650,
    '定安县': 32649,
    '定西市': 32648,
    '东方市': 32649,
    '东莞市': 32649,
    '东营市': 32650,
    '鄂尔多斯市': 32649,
    '鄂州市': 32650,
    '防城港市': 32648,
    '佛山市': 32649,
    '福州市': 32650,
    '抚顺市': 32651,
    '抚州市': 32650,
    '阜新市': 32651,
    '阜阳市': 32650,
    '赣州市': 32650,
    '固原市': 32648,
    '广安市': 32648,
    '广元市': 32648,
    '广州市': 32649,
    '贵港市': 32649,
    '贵阳市': 32648,
    '桂林市': 32649,
    '哈尔滨市': 32652,
    '哈密市': 32646,
    '海东市': 32648,
    '海口市': 32649,
    '邯郸市': 32650,
    '汉中市': 32648,
    '杭州市': 32650,
    '合肥市': 32650,
    '和田地区': 32644,
    '河池市': 32648,
    '河源市': 32650,
    '菏泽市': 32650,
    '贺州市': 32649,
    '鹤壁市': 32650,
    '鹤岗市': 32652,
    '黑河市': 32652,
    '衡水市': 32650,
    '衡阳市': 32649,
    '呼和浩特市': 32649,
    '呼伦贝尔市': 32651,
    '胡杨河市': 32645,
    '葫芦岛市': 32651,
    '湖州市': 32650,
    '怀化市': 32649,
    '淮安市': 32650,
    '淮北市': 32650,
    '淮南市': 32650,
    '黄冈市': 32650,
    '黄山市': 32650,
    '黄石市': 32650,
    '惠州市': 32650,
    '鸡西市': 32653,
    '吉安市': 32650,
    '吉林市': 32652,
    '济南市': 32650,
    '济宁市': 32650,
    '济源市': 32649,
    '佳木斯市': 32653,
    '嘉兴市': 32651,
    '嘉峪关市': 32647,
    '江门市': 32649,
    '焦作市': 32649,
    '揭阳市': 32650,
    '金昌市': 32648,
    '金华市': 32650,
    '锦州市': 32651,
    '晋城市': 32649,
    '晋中市': 32649,
    '荆门市': 32649,
    '荆州市': 32649,
    '景德镇市': 32650,
    '九江市': 32650,
    '酒泉市': 32647,
    '喀什地区': 32643,
    '开封市': 32650,
    '可克达拉市': 32644,
    '克拉玛依市': 32645,
    '昆明市': 32648,
    '昆玉市': 32644,
    '拉萨市': 32646,
    '来宾市': 32649,
    '兰州市': 32648,
    '廊坊市': 32650,
    '乐山市': 32648,
    '丽江市': 32647,
    '丽水市': 32650,
    '连云港市': 32650,
    '辽阳市': 32651,
    '辽源市': 32651,
    '聊城市': 32650,
    '林芝市': 32646,
    '临沧市': 32647,
    '临汾市': 32649,
    '临高县': 32649,
    '临沂市': 32650,
    '柳州市': 32649,
    '六安市': 32650,
    '六盘水市': 32648,
    '龙岩市': 32650,
    '陇南市': 32648,
    '娄底市': 32649,
    '泸州市': 32648,
    '洛阳市': 32649,
    '漯河市': 32649,
    '吕梁市': 32649,
    '马鞍山市': 32650,
    '茂名市': 32649,
    '眉山市': 32648,
    '梅州市': 32650,
    '绵阳市': 32648,
    '牡丹江市': 32652,
    '那曲市': 32645,
    '南昌市': 32650,
    '南充市': 32648,
    '南京市': 32650,
    '南宁市': 32649,
    '南平市': 32650,
    '南通市': 32651,
    '南阳市': 32649,
    '内江市': 32648,
    '宁波市': 32651,
    '宁德市': 32650,
    '攀枝花市': 32647,
    '盘锦市': 32651,
    '平顶山市': 32649,
    '平凉市': 32648,
    '萍乡市': 32649,
    '莆田市': 32650,
    '濮阳市': 32650,
    '普洱市': 32647,
    '七台河市': 32652,
    '齐齐哈尔市': 32651,
    '潜江市': 32649,
    '钦州市': 32649,
    '秦皇岛市': 32650,
    '青岛市': 32651,
    '清远市': 32649,
    '庆阳市': 32648,
    '琼海市': 32649,
    '衢州市': 32650,
    '曲靖市': 32648,
    '泉州市': 32650,
    '日喀则市': 32645,
    '日照市': 32650,
    '三门峡市': 32649,
    '三明市': 32650,
    '三沙市': 32649,
    '三亚市': 32649,
    '厦门市': 32650,
    '山南市': 32646,
    '汕头市': 32650,
    '汕尾市': 32650,
    '商洛市': 32649,
    '商丘市': 32650,
    '上海市': 32651,
    '上饶市': 32650,
    '韶关市': 32649,
    '邵阳市': 32649,
    '绍兴市': 32651,
    '深圳市': 32650,
    '沈阳市': 32651,
    '十堰市': 32649,
    '石河子市': 32645,
    '石家庄市': 32650,
    '石嘴山市': 32648,
    '双河市': 32644,
    '双鸭山市': 32653,
    '朔州市': 32649,
    '四平市': 32651,
    '松原市': 32651,
    '苏州市': 32651,
    '绥化市': 32652,
    '随州市': 32649,
    '遂宁市': 32648,
    '台北市': 32651,
    '台湾省': 32651,
    '台州市': 32651,
    '太原市': 32649,
    '泰安市': 32650,
    '泰州市': 32651,
    '唐山市': 32650,
    '天津市': 32650,
    '天门市': 32649,
    '天水市': 32648,
    '铁岭市': 32651,
    '铁门关市': 32645,
    '通化市': 32651,
    '通辽市': 32651,
    '铜川市': 32649,
    '铜陵市': 32650,
    '铜仁市': 32649,
    '图木舒克市': 32644,
    '吐鲁番市': 32645,
    '屯昌县': 32649,
    '万宁市': 32649,
    '威海市': 32651,
    '潍坊市': 32650,
    '渭南市': 32649,
    '温州市': 32651,
    '文昌市': 32649,
    '乌海市': 32648,
    '乌兰察布市': 32649,
    '乌鲁木齐市': 32645,
    '无锡市': 32651,
    '芜湖市': 32650,
    '吴忠市': 32648,
    '梧州市': 32649,
    '五家渠市': 32645,
    '五指山市': 32649,
    '武汉市': 32650,
    '武威市': 32648,
    '西安市': 32649,
    '西宁市': 32647,
    '仙桃市': 32649,
    '咸宁市': 32650,
    '咸阳市': 32649,
    '湘潭市': 32649,
    '襄阳市': 32649,
    '孝感市': 32649,
    '忻州市': 32649,
    '新乡市': 32650,
    '新余市': 32650,
    '信阳市': 32650,
    '邢台市': 32650,
    '兴安盟': 32651,
    '宿迁市': 32650,
    '宿州市': 32650,
    '徐州市': 32650,
    '许昌市': 32649,
    '宣城市': 32650,
    '雅安市': 32648,
    '烟台市': 32651,
    '延安市': 32649,
    '盐城市': 32651,
    '扬州市': 32650,
    '阳江市': 32649,
    '阳泉市': 32649,
    '伊春市': 32652,
    '宜宾市': 32648,
    '宜昌市': 32649,
    '宜春市': 32650,
    '益阳市': 32649,
    '银川市': 32648,
    '鹰潭市': 32650,
    '营口市': 32651,
    '永州市': 32649,
    '榆林市': 32649,
    '玉林市': 32649,
    '玉溪市': 32648,
    '岳阳市': 32649,
    '云浮市': 32649,
    '运城市': 32649,
    '枣庄市': 32650,
    '湛江市': 32649,
    '张家界市': 32649,
    '张家口市': 32650,
    '张掖市': 32647,
    '漳州市': 32650,
    '长春市': 32651,
    '长沙市': 32649,
    '长治市': 32649,
    '昭通市': 32648,
    '肇庆市': 32649,
    '镇江市': 32650,
    '郑州市': 32649,
    '中山市': 32649,
    '中卫市': 32648,
    '重庆市': 32648,
    '舟山市': 32651,
    '周口市': 32650,
    '珠海市': 32649,
    '株洲市': 32649,
    '驻马店市': 32650,
    '资阳市': 32648,
    '淄博市': 32650,
    '自贡市': 32648,
    '遵义市': 32648}

city_code = {
    '北京市': 110000,
    '天津市': 120000,
    '石家庄市': 130100,
    '辛集市': 130181,
    '晋州市': 130183,
    '新乐市': 130184,
    '唐山市': 130200,
    '遵化市': 130281,
    '迁安市': 130283,
    '秦皇岛市': 130300,
    '邯郸市': 130400,
    '武安市': 130481,
    '邢台市': 130500,
    '南宫市': 130581,
    '沙河市': 130582,
    '保定市': 130600,
    '涿州市': 130681,
    '定州市': 130682,
    '安国市': 130683,
    '高碑店市': 130684,
    '张家口市': 130700,
    '承德市': 130800,
    '平泉市': 130881,
    '沧州市': 130900,
    '泊头市': 130981,
    '任丘市': 130982,
    '黄骅市': 130983,
    '河间市': 130984,
    '廊坊市': 131000,
    '霸州市': 131081,
    '三河市': 131082,
    '衡水市': 131100,
    '深州市': 131182,
    '太原市': 140100,
    '古交市': 140181,
    '大同市': 140200,
    '阳泉市': 140300,
    '长治市': 140400,
    '潞城市': 140481,
    '晋城市': 140500,
    '高平市': 140581,
    '朔州市': 140600,
    '晋中市': 140700,
    '介休市': 140781,
    '运城市': 140800,
    '永济市': 140881,
    '河津市': 140882,
    '忻州市': 140900,
    '原平市': 140981,
    '临汾市': 141000,
    '侯马市': 141081,
    '霍州市': 141082,
    '吕梁市': 141100,
    '孝义市': 141181,
    '汾阳市': 141182,
    '呼和浩特市': 150100,
    '包头市': 150200,
    '乌海市': 150300,
    '赤峰市': 150400,
    '通辽市': 150500,
    '霍林郭勒市': 150581,
    '鄂尔多斯市': 150600,
    '呼伦贝尔市': 150700,
    '满洲里市': 150781,
    '牙克石市': 150782,
    '扎兰屯市': 150783,
    '额尔古纳市': 150784,
    '根河市': 150785,
    '巴彦淖尔市': 150800,
    '乌兰察布市': 150900,
    '丰镇市': 150981,
    '乌兰浩特市': 152201,
    '阿尔山市': 152202,
    '二连浩特市': 152501,
    '锡林浩特市': 152502,
    '沈阳市': 210100,
    '新民市': 210181,
    '大连市': 210200,
    '瓦房店市': 210281,
    '庄河市': 210283,
    '鞍山市': 210300,
    '海城市': 210381,
    '抚顺市': 210400,
    '本溪市': 210500,
    '丹东市': 210600,
    '东港市': 210681,
    '凤城市': 210682,
    '锦州市': 210700,
    '凌海市': 210781,
    '北镇市': 210782,
    '营口市': 210800,
    '盖州市': 210881,
    '大石桥市': 210882,
    '阜新市': 210900,
    '辽阳市': 211000,
    '灯塔市': 211081,
    '盘锦市': 211100,
    '铁岭市': 211200,
    '调兵山市': 211281,
    '开原市': 211282,
    '朝阳市': 211300,
    '北票市': 211381,
    '凌源市': 211382,
    '葫芦岛市': 211400,
    '兴城市': 211481,
    '长春市': 220100,
    '榆树市': 220182,
    '德惠市': 220183,
    '吉林市': 220200,
    '蛟河市': 220281,
    '桦甸市': 220282,
    '舒兰市': 220283,
    '磐石市': 220284,
    '四平市': 220300,
    '公主岭市': 220381,
    '双辽市': 220382,
    '辽源市': 220400,
    '通化市': 220500,
    '梅河口市': 220581,
    '集安市': 220582,
    '白山市': 220600,
    '临江市': 220681,
    '松原市': 220700,
    '扶余市': 220781,
    '白城市': 220800,
    '洮南市': 220881,
    '大安市': 220882,
    '延吉市': 222401,
    '图们市': 222402,
    '敦化市': 222403,
    '珲春市': 222404,
    '龙井市': 222405,
    '和龙市': 222406,
    '哈尔滨市': 230100,
    '尚志市': 230183,
    '五常市': 230184,
    '齐齐哈尔市': 230200,
    '讷河市': 230281,
    '鸡西市': 230300,
    '虎林市': 230381,
    '密山市': 230382,
    '鹤岗市': 230400,
    '双鸭山市': 230500,
    '大庆市': 230600,
    '伊春市': 230700,
    '铁力市': 230781,
    '佳木斯市': 230800,
    '同江市': 230881,
    '富锦市': 230882,
    '抚远市': 230883,
    '七台河市': 230900,
    '牡丹江市': 231000,
    '绥芬河市': 231081,
    '海林市': 231083,
    '宁安市': 231084,
    '穆棱市': 231085,
    '东宁市': 231086,
    '黑河市': 231100,
    '北安市': 231181,
    '五大连池市': 231182,
    '绥化市': 231200,
    '安达市': 231281,
    '肇东市': 231282,
    '海伦市': 231283,
    '上海市': 310000,
    '南京市': 320100,
    '无锡市': 320200,
    '江阴市': 320281,
    '宜兴市': 320282,
    '徐州市': 320300,
    '新沂市': 320381,
    '邳州市': 320382,
    '常州市': 320400,
    '溧阳市': 320481,
    '苏州市': 320500,
    '常熟市': 320581,
    '张家港市': 320582,
    '昆山市': 320583,
    '太仓市': 320585,
    '南通市': 320600,
    '启东市': 320681,
    '如皋市': 320682,
    '海门市': 320684,
    '连云港市': 320700,
    '淮安市': 320800,
    '盐城市': 320900,
    '东台市': 320981,
    '扬州市': 321000,
    '仪征市': 321081,
    '高邮市': 321084,
    '镇江市': 321100,
    '丹阳市': 321181,
    '扬中市': 321182,
    '句容市': 321183,
    '泰州市': 321200,
    '兴化市': 321281,
    '靖江市': 321282,
    '泰兴市': 321283,
    '宿迁市': 321300,
    '杭州市': 330100,
    '建德市': 330182,
    '宁波市': 330200,
    '余姚市': 330281,
    '慈溪市': 330282,
    '温州市': 330300,
    '瑞安市': 330381,
    '乐清市': 330382,
    '嘉兴市': 330400,
    '海宁市': 330481,
    '平湖市': 330482,
    '桐乡市': 330483,
    '湖州市': 330500,
    '绍兴市': 330600,
    '诸暨市': 330681,
    '嵊州市': 330683,
    '金华市': 330700,
    '兰溪市': 330781,
    '义乌市': 330782,
    '东阳市': 330783,
    '永康市': 330784,
    '衢州市': 330800,
    '江山市': 330881,
    '舟山市': 330900,
    '台州市': 331000,
    '温岭市': 331081,
    '临海市': 331082,
    '玉环市': 331083,
    '丽水市': 331100,
    '龙泉市': 331181,
    '合肥市': 340100,
    '巢湖市': 340181,
    '芜湖市': 340200,
    '蚌埠市': 340300,
    '淮南市': 340400,
    '马鞍山市': 340500,
    '淮北市': 340600,
    '铜陵市': 340700,
    '安庆市': 340800,
    '桐城市': 340881,
    '黄山市': 341000,
    '滁州市': 341100,
    '天长市': 341181,
    '明光市': 341182,
    '阜阳市': 341200,
    '界首市': 341282,
    '宿州市': 341300,
    '六安市': 341500,
    '亳州市': 341600,
    '池州市': 341700,
    '宣城市': 341800,
    '宁国市': 341881,
    '福州市': 350100,
    '福清市': 350181,
    '厦门市': 350200,
    '莆田市': 350300,
    '三明市': 350400,
    '永安市': 350481,
    '泉州市': 350500,
    '石狮市': 350581,
    '晋江市': 350582,
    '南安市': 350583,
    '漳州市': 350600,
    '龙海市': 350681,
    '南平市': 350700,
    '邵武市': 350781,
    '武夷山市': 350782,
    '建瓯市': 350783,
    '龙岩市': 350800,
    '漳平市': 350881,
    '宁德市': 350900,
    '福安市': 350981,
    '福鼎市': 350982,
    '南昌市': 360100,
    '景德镇市': 360200,
    '乐平市': 360281,
    '萍乡市': 360300,
    '九江市': 360400,
    '瑞昌市': 360481,
    '共青城市': 360482,
    '庐山市': 360483,
    '新余市': 360500,
    '鹰潭市': 360600,
    '贵溪市': 360681,
    '赣州市': 360700,
    '瑞金市': 360781,
    '吉安市': 360800,
    '井冈山市': 360881,
    '宜春市': 360900,
    '丰城市': 360981,
    '樟树市': 360982,
    '高安市': 360983,
    '抚州市': 361000,
    '上饶市': 361100,
    '德兴市': 361181,
    '济南市': 370100,
    '青岛市': 370200,
    '胶州市': 370281,
    '平度市': 370283,
    '莱西市': 370285,
    '淄博市': 370300,
    '枣庄市': 370400,
    '滕州市': 370481,
    '东营市': 370500,
    '烟台市': 370600,
    '龙口市': 370681,
    '莱阳市': 370682,
    '莱州市': 370683,
    '蓬莱市': 370684,
    '招远市': 370685,
    '栖霞市': 370686,
    '海阳市': 370687,
    '潍坊市': 370700,
    '青州市': 370781,
    '诸城市': 370782,
    '寿光市': 370783,
    '安丘市': 370784,
    '高密市': 370785,
    '昌邑市': 370786,
    '济宁市': 370800,
    '曲阜市': 370881,
    '邹城市': 370883,
    '泰安市': 370900,
    '新泰市': 370982,
    '肥城市': 370983,
    '威海市': 371000,
    '荣成市': 371082,
    '乳山市': 371083,
    '日照市': 371100,
    '莱芜市': 371200,
    '临沂市': 371300,
    '德州市': 371400,
    '乐陵市': 371481,
    '禹城市': 371482,
    '聊城市': 371500,
    '临清市': 371581,
    '滨州市': 371600,
    '菏泽市': 371700,
    '郑州市': 410100,
    '巩义市': 410181,
    '荥阳市': 410182,
    '新密市': 410183,
    '新郑市': 410184,
    '登封市': 410185,
    '开封市': 410200,
    '洛阳市': 410300,
    '偃师市': 410381,
    '平顶山市': 410400,
    '舞钢市': 410481,
    '汝州市': 410482,
    '安阳市': 410500,
    '林州市': 410581,
    '鹤壁市': 410600,
    '新乡市': 410700,
    '卫辉市': 410781,
    '辉县市': 410782,
    '焦作市': 410800,
    '沁阳市': 410882,
    '孟州市': 410883,
    '濮阳市': 410900,
    '许昌市': 411000,
    '禹州市': 411081,
    '长葛市': 411082,
    '漯河市': 411100,
    '三门峡市': 411200,
    '义马市': 411281,
    '灵宝市': 411282,
    '南阳市': 411300,
    '邓州市': 411381,
    '商丘市': 411400,
    '永城市': 411481,
    '信阳市': 411500,
    '周口市': 411600,
    '项城市': 411681,
    '驻马店市': 411700,
    '济源市': 419001,
    '武汉市': 420100,
    '黄石市': 420200,
    '大冶市': 420281,
    '十堰市': 420300,
    '丹江口市': 420381,
    '宜昌市': 420500,
    '宜都市': 420581,
    '当阳市': 420582,
    '枝江市': 420583,
    '襄阳市': 420600,
    '老河口市': 420682,
    '枣阳市': 420683,
    '宜城市': 420684,
    '鄂州市': 420700,
    '荆门市': 420800,
    '钟祥市': 420881,
    '孝感市': 420900,
    '应城市': 420981,
    '安陆市': 420982,
    '汉川市': 420984,
    '荆州市': 421000,
    '石首市': 421081,
    '洪湖市': 421083,
    '松滋市': 421087,
    '黄冈市': 421100,
    '麻城市': 421181,
    '武穴市': 421182,
    '咸宁市': 421200,
    '赤壁市': 421281,
    '随州市': 421300,
    '广水市': 421381,
    '恩施市': 422801,
    '利川市': 422802,
    '仙桃市': 429004,
    '潜江市': 429005,
    '天门市': 429006,
    '长沙市': 430100,
    '浏阳市': 430181,
    '宁乡市': 430182,
    '株洲市': 430200,
    '醴陵市': 430281,
    '湘潭市': 430300,
    '湘乡市': 430381,
    '韶山市': 430382,
    '衡阳市': 430400,
    '耒阳市': 430481,
    '常宁市': 430482,
    '邵阳市': 430500,
    '武冈市': 430581,
    '岳阳市': 430600,
    '汨罗市': 430681,
    '临湘市': 430682,
    '常德市': 430700,
    '津市市': 430781,
    '张家界市': 430800,
    '益阳市': 430900,
    '沅江市': 430981,
    '郴州市': 431000,
    '资兴市': 431081,
    '永州市': 431100,
    '怀化市': 431200,
    '洪江市': 431281,
    '娄底市': 431300,
    '冷水江市': 431381,
    '涟源市': 431382,
    '吉首市': 433101,
    '广州市': 440100,
    '韶关市': 440200,
    '乐昌市': 440281,
    '南雄市': 440282,
    '深圳市': 440300,
    '珠海市': 440400,
    '汕头市': 440510,
    '佛山市': 440600,
    '江门市': 440700,
    '台山市': 440781,
    '开平市': 440783,
    '鹤山市': 440784,
    '恩平市': 440785,
    '湛江市': 440800,
    '廉江市': 440881,
    '雷州市': 440882,
    '吴川市': 440883,
    '茂名市': 440900,
    '高州市': 440981,
    '化州市': 440982,
    '信宜市': 440983,
    '肇庆市': 441200,
    '四会市': 441284,
    '惠州市': 441300,
    '梅州市': 441400,
    '兴宁市': 441481,
    '汕尾市': 441500,
    '陆丰市': 441581,
    '河源市': 441600,
    '阳江市': 441700,
    '阳春市': 441781,
    '清远市': 441800,
    '英德市': 441881,
    '连州市': 441882,
    '东莞市': 441900,
    '中山市': 442000,
    '潮州市': 445100,
    '揭阳市': 445200,
    '普宁市': 445281,
    '云浮市': 445300,
    '罗定市': 445381,
    '南宁市': 450100,
    '柳州市': 450200,
    '桂林市': 450300,
    '梧州市': 450400,
    '岑溪市': 450481,
    '北海市': 450500,
    '防城港市': 450600,
    '东兴市': 450681,
    '钦州市': 450700,
    '贵港市': 450800,
    '桂平市': 450881,
    '玉林市': 450900,
    '北流市': 450981,
    '百色市': 451000,
    '靖西市': 451081,
    '贺州市': 451100,
    '河池市': 451200,
    '来宾市': 451300,
    '合山市': 451381,
    '崇左市': 451400,
    '凭祥市': 451481,
    '海口市': 460100,
    '三亚市': 460200,
    '三沙市': 460300,
    '儋州市': 460400,
    '五指山市': 469001,
    '琼海市': 469002,
    '文昌市': 469005,
    '万宁市': 469006,
    '东方市': 469007,
    '重庆市': 500000,
    '重庆市郊县': 500200,
    '成都市': 510100,
    '都江堰市': 510181,
    '彭州市': 510182,
    '邛崃市': 510183,
    '崇州市': 510184,
    '简阳市': 510185,
    '自贡市': 510300,
    '攀枝花市': 510400,
    '泸州市': 510500,
    '德阳市': 510600,
    '广汉市': 510681,
    '什邡市': 510682,
    '绵竹市': 510683,
    '绵阳市': 510700,
    '江油市': 510781,
    '广元市': 510800,
    '遂宁市': 510900,
    '内江市': 511000,
    '隆昌市': 511083,
    '乐山市': 511100,
    '峨眉山市': 511181,
    '南充市': 511300,
    '阆中市': 511381,
    '眉山市': 511400,
    '宜宾市': 511500,
    '广安市': 511600,
    '华蓥市': 511681,
    '达州市': 511700,
    '万源市': 511781,
    '雅安市': 511800,
    '巴中市': 511900,
    '资阳市': 512000,
    '马尔康市': 513201,
    '九寨沟市': 513225,
    '康定市': 513301,
    '西昌市': 513401,
    '贵阳市': 520100,
    '清镇市': 520181,
    '六盘水市': 520200,
    '盘州市': 520281,
    '遵义市': 520300,
    '赤水市': 520381,
    '仁怀市': 520382,
    '安顺市': 520400,
    '毕节市': 520500,
    '铜仁市': 520600,
    '兴义市': 522301,
    '凯里市': 522601,
    '都匀市': 522701,
    '福泉市': 522702,
    '昆明市': 530100,
    '安宁市': 530181,
    '曲靖市': 530300,
    '宣威市': 530381,
    '玉溪市': 530400,
    '保山市': 530500,
    '腾冲市': 530581,
    '昭通市': 530600,
    '丽江市': 530700,
    '普洱市': 530800,
    '临沧市': 530900,
    '楚雄市': 532301,
    '个旧市': 532501,
    '开远市': 532502,
    '蒙自市': 532503,
    '弥勒市': 532504,
    '文山市': 532601,
    '景洪市': 532801,
    '大理市': 532901,
    '瑞丽市': 533102,
    '芒市': 533103,
    '泸水市': 533301,
    '香格里拉市': 533401,
    '拉萨市': 540100,
    '日喀则市': 540200,
    '昌都市': 540300,
    '林芝市': 540400,
    '山南市': 540500,
    '那曲市': 540600,
    '西安市': 610100,
    '铜川市': 610200,
    '宝鸡市': 610300,
    '咸阳市': 610400,
    '兴平市': 610481,
    '渭南市': 610500,
    '韩城市': 610581,
    '华阴市': 610582,
    '延安市': 610600,
    '汉中市': 610700,
    '榆林市': 610800,
    '神木市': 610881,
    '安康市': 610900,
    '商洛市': 611000,
    '兰州市': 620100,
    '嘉峪关市': 620200,
    '金昌市': 620300,
    '白银市': 620400,
    '天水市': 620500,
    '武威市': 620600,
    '张掖市': 620700,
    '平凉市': 620800,
    '酒泉市': 620900,
    '玉门市': 620981,
    '敦煌市': 620982,
    '庆阳市': 621000,
    '定西市': 621100,
    '陇南市': 621200,
    '临夏市': 622901,
    '合作市': 623001,
    '西宁市': 630100,
    '海东市': 630200,
    '玉树市': 632701,
    '格尔木市': 632801,
    '德令哈市': 632802,
    '银川市': 640100,
    '灵武市': 640181,
    '石嘴山市': 640200,
    '吴忠市': 640300,
    '青铜峡市': 640381,
    '固原市': 640400,
    '中卫市': 640500,
    '乌鲁木齐市': 650100,
    '克拉玛依市': 650200,
    '吐鲁番市': 650400,
    '哈密市': 650500,
    '昌吉市': 652301,
    '阜康市': 652302,
    '博乐市': 652701,
    '阿拉山口市': 652702,
    '库尔勒市': 652801,
    '阿克苏市': 652901,
    '阿图什市': 653001,
    '喀什市': 653101,
    '和田市': 653201,
    '伊宁市': 654002,
    '奎屯市': 654003,
    '霍尔果斯市': 654004,
    '塔城市': 654201,
    '乌苏市': 654202,
    '阿勒泰市': 654301,
    '石河子市': 659001,
    '阿拉尔市': 659002,
    '图木舒克市': 659003,
    '五家渠市': 659004,
    '北屯市': 659005,
    '铁门关市': 659006,
    '双河市': 659007,
    '可克达拉市': 659008,
    '昆玉市': 659009}

