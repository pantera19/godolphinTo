var nameMap = {
    'Afghanistan':'Afghanistan',
    'Angola':'Angola',
    'Albania':'Albania',
    'United Arab Emirates':'United Arab Emirates',
    'Argentina':'Argentina',
    'Armenia':'Armenia',
    'French Southern and Antarctic Lands':'French Southern and Antarctic Lands',
    'Australia':'Australia',
    'Austria':'Austria',
    'Azerbaijan':'Azerbaijan',
    'Burundi':'Burundi',
    'Belgium':'Belgium',
    'Benin':'Benin',
    'Burkina Faso':'Burkina Faso',
    'Bangladesh':'Bangladesh',
    'Bulgaria':'Bulgaria',
    'The Bahamas':'The Bahamas',
    'Bosnia and Herzegovina':'Bosnia and Herzegovina',
    'Belarus':'Belarus',
    'Belize':'Belize',
    'Bermuda':'Bermuda',
    'Bolivia':'Bolivia',
    'Brazil':'Brazil',
    'Brunei':'Brunei',
    'Bhutan':'Bhutan',
    'Botswana':'Botswana',
    'Central African Republic':'Central African Republic',
    'Canada':'Canada',
    'Switzerland':'Switzerland',
    'Chile':'Chile',
    'China':'China',
    'Ivory Coast':'Ivory Coast',
    'Cameroon':'Cameroon',
    'Democratic Republic of the Congo':'Democratic Republic of the Congo',
    'Republic of the Congo':'Republic of the Congo',
    'Colombia':'Colombia',
    'Costa Rica':'Costa Rica',
    'Cuba':'Cuba',
    'Northern Cyprus':'Northern Cyprus',
    'Cyprus':'Cyprus',
    'Czech Republic':'Czech Republic',
    'Germany':'Germany',
    'Djibouti':'Djibouti',
    'Denmark':'Denmark',
    'Dominican Republic':'Dominican Republic',
    'Algeria':'Algeria',
    'Ecuador':'Ecuador',
    'Egypt':'Egypt',
    'Eritrea':'Eritrea',
    'Spain':'Spain',
    'Estonia':'Estonia',
    'Ethiopia':'Ethiopia',
    'Finland':'Finland',
    'Fiji':'Fiji',
    'Falkland Islands':'Falkland Islands',
    'France':'France',
    'Gabon':'Gabon',
    'United Kingdom':'United Kingdom',
    'Georgia':'Georgia',
    'Ghana':'Ghana',
    'Guinea':'Guinea',
    'Gambia':'Gambia',
    'Guinea Bissau':'Guinea Bissau',
    'Equatorial Guinea':'Equatorial Guinea',
    'Greece':'Greece',
    'Greenland':'Greenland',
    'Guatemala':'Guatemala',
    'French Guiana':'French Guiana',
    'Guyana':'Guyana',
    'Honduras':'Honduras',
    'Croatia':'Croatia',
    'Haiti':'Haiti',
    'Hungary':'Hungary',
    'Indonesia':'Indonesia',
    'India':'India',
    'Ireland':'Ireland',
    'Iran':'Iran',
    'Iraq':'Iraq',
    'Iceland':'Iceland',
    'Israel':'Israel',
    'Italy':'Italy',
    'Jamaica':'Jamaica',
    'Jordan':'Jordan',
    'Japan':'Japan',
    'Kazakhstan':'Kazakhstan',
    'Kenya':'Kenya',
    'Kyrgyzstan':'Kyrgyzstan',
    'Cambodia':'Cambodia',
    'South Korea':'South Korea',
    'Kosovo':'Kosovo',
    'Kuwait':'Kuwait',
    'Laos':'Laos',
    'Lebanon':'Lebanon',
    'Liberia':'Liberia',
    'Libya':'Libya',
    'Sri Lanka':'Sri Lanka',
    'Lesotho':'Lesotho',
    'Lithuania':'Lithuania',
    'Luxembourg':'Luxembourg',
    'Latvia':'Latvia',
    'Morocco':'Morocco',
    'Moldova':'Moldova',
    'Madagascar':'Madagascar',
    'Mexico':'Mexico',
    'Macedonia':'Macedonia',
    'Mali':'Mali',
    'Myanmar':'Myanmar',
    'Montenegro':'Montenegro',
    'Mongolia':'Mongolia',
    'Mozambique':'Mozambique',
    'Mauritania':'Mauritania',
    'Malawi':'Malawi',
    'Malaysia':'Malaysia',
    'Namibia':'Namibia',
    'New Caledonia':'New Caledonia',
    'Niger':'Niger',
    'Nigeria':'Nigeria',
    'Nicaragua':'Nicaragua',
    'Netherlands':'Netherlands',
    'Norway':'Norway',
    'Nepal':'Nepal',
    'New Zealand':'New Zealand',
    'Oman':'Oman',
    'Pakistan':'Pakistan',
    'Panama':'Panama',
    'Peru':'Peru',
    'Philippines':'Philippines',
    'Papua New Guinea':'Papua New Guinea',
    'Poland':'Poland',
    'Puerto Rico':'Puerto Rico',
    'North Korea':'North Korea',
    'Portugal':'Portugal',
    'Paraguay':'Paraguay',
    'Qatar':'Qatar',
    'Romania':'Romania',
    'Russia':'Russia',
    'Rwanda':'Rwanda',
    'Western Sahara':'Western Sahara',
    'Saudi Arabia':'Saudi Arabia',
    'Sudan':'Sudan',
    'South Sudan':'South Sudan',
    'Senegal':'Senegal',
    'Solomon Islands':'Solomon Islands',
    'Sierra Leone':'Sierra Leone',
    'El Salvador':'El Salvador',
    'Somaliland':'Somaliland',
    'Somalia':'Somalia',
    'Republic of Serbia':'Republic of Serbia',
    'Suriname':'Suriname',
    'Slovakia':'Slovakia',
    'Slovenia':'Slovenia',
    'Sweden':'Sweden',
    'Swaziland':'Swaziland',
    'Syria':'Syria',
    'Chad':'Chad',
    'Togo':'Togo',
    'Thailand':'Thailand',
    'Tajikistan':'Tajikistan',
    'Turkmenistan':'Turkmenistan',
    'East Timor':'East Timor',
    'Trinidad and Tobago':'Trinidad and Tobago',
    'Tunisia':'Tunisia',
    'Turkey':'Turkey',
    'United Republic of Tanzania':'United Republic of Tanzania',
    'Uganda':'Uganda',
    'Ukraine':'Ukraine',
    'Uruguay':'Uruguay',
    'United States of America':'United States of America',
    'Uzbekistan':'Uzbekistan',
    'Venezuela':'Venezuela',
    'Vietnam':'Vietnam',
    'Vanuatu':'Vanuatu',
    'West Bank':'West Bank',
    'Yemen':'Yemen',
    'South Africa':'South Africa',
    'Zambia':'Zambia',
    'Zimbabwe':'Zimbabwe'
};

var nameMap_CH = {
    'Afghanistan':'阿富汗',
    'Angola':'安哥拉',
    'Albania':'阿尔巴尼亚',
    'United Arab Emirates':'阿联酋',
    'Argentina':'阿根廷',
    'Armenia':'亚美尼亚',
    'French Southern and Antarctic Lands':'法属南半球和南极领地',
    'Australia':'澳大利亚',
    'Austria':'奥地利',
    'Azerbaijan':'阿塞拜疆',
    'Burundi':'布隆迪',
    'Belgium':'比利时',
    'Benin':'贝宁',
    'Burkina Faso':'布基纳法索',
    'Bangladesh':'孟加拉国',
    'Bulgaria':'保加利亚',
    'The Bahamas':'巴哈马',
    'Bosnia and Herzegovina':'波斯尼亚和黑塞哥维那',
    'Belarus':'白俄罗斯',
    'Belize':'伯利兹',
    'Bermuda':'百慕大',
    'Bolivia':'玻利维亚',
    'Brazil':'巴西',
    'Brunei':'文莱',
    'Bhutan':'不丹',
    'Botswana':'博茨瓦纳',
    'Central African Republic':'中非共和国',
    'Canada':'加拿大',
    'Switzerland':'瑞士',
    'Chile':'智利',
    'China':'中国',
    'Ivory Coast':'象牙海岸',
    'Cameroon':'喀麦隆',
    'Democratic Republic of the Congo':'刚果民主共和国',
    'Republic of the Congo':'刚果共和国',
    'Colombia':'哥伦比亚',
    'Costa Rica':'哥斯达黎加',
    'Cuba':'古巴',
    'Northern Cyprus':'北塞浦路斯',
    'Cyprus':'塞浦路斯',
    'Czech Republic':'捷克共和国',
    'Germany':'德国',
    'Djibouti':'吉布提',
    'Denmark':'丹麦',
    'Dominican Republic':'多明尼加共和国',
    'Algeria':'阿尔及利亚',
    'Ecuador':'厄瓜多尔',
    'Egypt':'埃及',
    'Eritrea':'厄立特里亚',
    'Spain':'西班牙',
    'Estonia':'爱沙尼亚',
    'Ethiopia':'埃塞俄比亚',
    'Finland':'芬兰',
    'Fiji':'斐',
    'Falkland Islands':'福克兰群岛',
    'France':'法国',
    'Gabon':'加蓬',
    'United Kingdom':'英国',
    'Georgia':'格鲁吉亚',
    'Ghana':'加纳',
    'Guinea':'几内亚',
    'Gambia':'冈比亚',
    'Guinea Bissau':'几内亚比绍',
    'Equatorial Guinea':'赤道几内亚',
    'Greece':'希腊',
    'Greenland':'格陵兰',
    'Guatemala':'危地马拉',
    'French Guiana':'法属圭亚那',
    'Guyana':'圭亚那',
    'Honduras':'洪都拉斯',
    'Croatia':'克罗地亚',
    'Haiti':'海地',
    'Hungary':'匈牙利',
    'Indonesia':'印尼',
    'India':'印度',
    'Ireland':'爱尔兰',
    'Iran':'伊朗',
    'Iraq':'伊拉克',
    'Iceland':'冰岛',
    'Israel':'以色列',
    'Italy':'意大利',
    'Jamaica':'牙买加',
    'Jordan':'约旦',
    'Japan':'日本',
    'Kazakhstan':'哈萨克斯坦',
    'Kenya':'肯尼亚',
    'Kyrgyzstan':'吉尔吉斯斯坦',
    'Cambodia':'柬埔寨',
    'South Korea':'韩国',
    'Kosovo':'科索沃',
    'Kuwait':'科威特',
    'Laos':'老挝',
    'Lebanon':'黎巴嫩',
    'Liberia':'利比里亚',
    'Libya':'利比亚',
    'Sri Lanka':'斯里兰卡',
    'Lesotho':'莱索托',
    'Lithuania':'立陶宛',
    'Luxembourg':'卢森堡',
    'Latvia':'拉脱维亚',
    'Morocco':'摩洛哥',
    'Moldova':'摩尔多瓦',
    'Madagascar':'马达加斯加',
    'Mexico':'墨西哥',
    'Macedonia':'马其顿',
    'Mali':'马里',
    'Myanmar':'缅甸',
    'Montenegro':'黑山',
    'Mongolia':'蒙古',
    'Mozambique':'莫桑比克',
    'Mauritania':'毛里塔尼亚',
    'Malawi':'马拉维',
    'Malaysia':'马来西亚',
    'Namibia':'纳米比亚',
    'New Caledonia':'新喀里多尼亚',
    'Niger':'尼日尔',
    'Nigeria':'尼日利亚',
    'Nicaragua':'尼加拉瓜',
    'Netherlands':'荷兰',
    'Norway':'挪威',
    'Nepal':'尼泊尔',
    'New Zealand':'新西兰',
    'Oman':'阿曼',
    'Pakistan':'巴基斯坦',
    'Panama':'巴拿马',
    'Peru':'秘鲁',
    'Philippines':'菲律宾',
    'Papua New Guinea':'巴布亚新几内亚',
    'Poland':'波兰',
    'Puerto Rico':'波多黎各',
    'North Korea':'北朝鲜',
    'Portugal':'葡萄牙',
    'Paraguay':'巴拉圭',
    'Qatar':'卡塔尔',
    'Romania':'罗马尼亚',
    'Russia':'俄罗斯',
    'Rwanda':'卢旺达',
    'Western Sahara':'西撒哈拉',
    'Saudi Arabia':'沙特阿拉伯',
    'Sudan':'苏丹',
    'South Sudan':'南苏丹',
    'Senegal':'塞内加尔',
    'Solomon Islands':'所罗门群岛',
    'Sierra Leone':'塞拉利昂',
    'El Salvador':'萨尔瓦多',
    'Somaliland':'索马里兰',
    'Somalia':'索马里',
    'Republic of Serbia':'塞尔维亚共和国',
    'Suriname':'苏里南',
    'Slovakia':'斯洛伐克',
    'Slovenia':'斯洛文尼亚',
    'Sweden':'瑞典',
    'Swaziland':'斯威士兰',
    'Syria':'叙利亚',
    'Chad':'乍得',
    'Togo':'多哥',
    'Thailand':'泰国',
    'Tajikistan':'塔吉克斯坦',
    'Turkmenistan':'土库曼斯坦',
    'East Timor':'东帝汶',
    'Trinidad and Tobago':'特里尼达和多巴哥',
    'Tunisia':'突尼斯',
    'Turkey':'土耳其',
    'United Republic of Tanzania':'坦桑尼亚联合共和国',
    'Uganda':'乌干达',
    'Ukraine':'乌克兰',
    'Uruguay':'乌拉圭',
    'United States of America':'美国',
    'Uzbekistan':'乌兹别克斯坦',
    'Venezuela':'委内瑞拉',
    'Vietnam':'越南',
    'Vanuatu':'瓦努阿图',
    'West Bank':'西岸',
    'Yemen':'也门',
    'South Africa':'南非',
    'Zambia':'赞比亚',
    'Zimbabwe':'津巴布韦'
};

var nameChinaMap = {
    '北京': 'BeiJing',
    '天津': 'TianJin',
    '上海': 'ShangHai',
    '重庆': 'ZhongQing',
    '河北': 'HeBei',
    '河南': 'HeNan',
    '云南': 'YunNan',
    '辽宁': 'LiaoNing',
    '黑龙江': 'HeiLongJiang',
    '湖南': 'HuNan',
    '安徽': 'AnHui',
    '山东': 'ShanDong',
    '新疆': 'XinJiang',
    '江苏': 'JiangSu',
    '浙江': 'ZheJiang',
    '江西': 'JiangXi',
    '湖北': 'HuBei',
    '广西': 'GuangXi',
    '甘肃': 'GanSu',
    '山西': 'ShanXi',
    '内蒙古': 'NeiMengGu',
    '陕西': 'ShanXi',
    '吉林': 'JiLin',
    '福建': 'FuJian',
    '贵州': 'GuiZhou',
    '广东': 'GuangDong',
    '青海': 'QingHai',
    '西藏': 'XiZang',
    '四川': 'SiChuan',
    '宁夏': 'NingXia',
    '海南': 'HaiNan',
    '台湾': 'TaiWan',
    '香港': 'XiangGang',
    '澳门': 'AoMen'
};

var nameChinaMap_CH = {
    '北京': '北京',
    '天津': '天津',
    '上海': '上海',
    '重庆': '重庆',
    '河北': '河北',
    '河南': '河南',
    '云南': '云南',
    '辽宁': '辽宁',
    '黑龙江': '黑龙江',
    '湖南': '湖南',
    '安徽': '安徽',
    '山东': '山东',
    '新疆': '新疆',
    '江苏': '江苏',
    '浙江': '浙江',
    '江西': '江西',
    '湖北': '湖北',
    '广西': '广西',
    '甘肃': '甘肃',
    '山西': '山西',
    '内蒙古': '内蒙古',
    '陕西': '陕西',
    '吉林': '吉林',
    '福建': '福建',
    '贵州': '贵州',
    '广东': '广东',
    '青海': '青海',
    '西藏': '西藏',
    '四川': '四川',
    '宁夏': '宁夏',
    '海南': '海南',
    '台湾': '台湾',
    '香港': '香港',
    '澳门': '澳门'
};

var itemTitle = 'Item Quantity';

$(function () {
    var url = location.href;
    if(url.indexOf('/ch/') > 0){
        itemTitle = "项目数量";
        nameMap = nameMap_CH;
        nameChinaMap = nameChinaMap_CH;
    }


    var myWorldChart = echarts.init(document.getElementById('worldMap'));
    /*myWorldChart.showLoading();//加载数据前显示的动画效果

    myWorldChart.hideLoading();//加载数据完成后隐藏动画*/

    myWorldChart.setOption({
        title: {
            text: '',
            subtext: '',
            sublink: '',
            left: 'center',
            top: 'top'
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                if(isNaN(params.value)){
                    return;
                }
                return params.seriesName + ' : ' + params.value;
            }
        },
        visualMap: {
            show:false,
            min: 0,
            max: 100,
            splitNumber: 2,
            color: ['#d94e5d']
        },
        series: [
            {
                name: itemTitle,
                type: 'map',
                mapType: 'world',
                roam: false,
                label:{
                    normal: {
                        show:false,
                        formatter: function (params) {
                            return nameMap[params.name];
                            /*return params.name;*/
                        }
                    },
                    emphasis: {
                        label:{
                            show:true
                        }
                    }
                },
                itemStyle: {
                    //正常时的样式
                    normal:{
                        borderWidth: 1,
                        borderColor: '#777',
                        areaColor: '#fff',
                        label: {show:true}
                    },
                    emphasis: {
                        borderWidth:1,
                        borderColor:'#ccc',
                        areaColor: '#ccc',
                        label: {
                            show: true,
                            textStyle: {
                                color: '#333'
                            }
                        }
                    }
                },
                data: world_data
            }
        ]
    });

    myWorldChart.on('click', function (params) {
        if(params.name != 'China')
            return;
        $('#worldMap').addClass('no-dis');
        $('#chinaMap,#backMap').removeClass('no-dis');
        loadChinaMap();
    });

});

$('#backMap').on('click', function () {
    $('#worldMap').removeClass('no-dis');
    $('#chinaMap,#backMap').addClass('no-dis');
    $('.news-list li').removeClass('no-dis');
});

function loadChinaMap(){
    var myChinaChart = echarts.init(document.getElementById('chinaMap'));

    myChinaChart.setOption({
        title: {
            text: '',
            subtext: '',
            left: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                if(isNaN(params.value)){
                    return;
                }
                return params.seriesName + ' : ' + params.value;
            }
        },
        visualMap: {
            show:false,
            min: 0,
            max: 100,
            splitNumber: 2,
            color: ['#d94e5d']
        },
        series: [
            {
                name: itemTitle,
                type: 'map',
                mapType: 'china',
                roam: false,
                label:{
                    normal: {
                        show:false,
                        formatter: function (params) {
                            return nameChinaMap[params.name];
                        }
                    },
                    emphasis: {
                        label:{
                            show:true
                        }
                    }
                },
                itemStyle: {
                    //正常时的样式
                    normal:{
                        borderWidth: 1,
                        borderColor: '#777',
                        areaColor: '#fff',
                        label: {show:true}
                    },
                    emphasis: {
                        borderWidth:1,
                        borderColor:'#ccc',
                        areaColor: '#ccc',
                        label: {
                            show: true,
                            textStyle: {
                                color: '#333'
                            }
                        }
                    }
                },
                data:china_data
            }
        ]
    });

    myChinaChart.on('click', function (params) {
        $('.news-list li').each(function (e) {
            if($(this).attr('china_name') == params.name)
                $(this).removeClass('no-dis');
            else
                $(this).addClass('no-dis');
        })
    });
}