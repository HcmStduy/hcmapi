import json

def get_commodity(commoditys):
    sub_str = ""
    for commodity in commoditys:
        id = commodity['CommodityId'] #商品id是主键
        categoryId_id = commodity['CategoryId'] #分类id外键
        commodityName = commodity['CommodityName']  #商品名称
        state = commodity['State']  #商品状态
        sellPrice = (commodity['SellPrice'])  #销售价格
        maxCommodityCount = commodity['MaxLimitCount']  #库存
        spec = commodity['Spec'] #商品规格
        smallPicture = commodity['SmallPic'] #商品小图
        showPicture = commodity['SmallPic'] #商品展示图片 ,先暂时用小图
        subTitle = commodity['SubTitle'] #商品二级标题
        canAddCart = commodity['CanAddToCart'] #能否加入购物车

        sub_str += "('%s','%s', '%s', '%s', %s,  %s, '%s', '%s','%s', '%s', %s),\n" % (id,categoryId_id,commodityName, state,sellPrice,  maxCommodityCount, spec, smallPicture, showPicture, subTitle,canAddCart)
    return sub_str

def changeSQl(name1,name2):
    with open(name1,'rb') as f:
        commodity_dict = json.load(f)
        all_commodity = commodity_dict['Data']['CommodityList']
        sql = 'INSERT INTO t_commodity(id,categoryId_id,commodityName, state,sellPrice,  maxCommodityCount, spec, smallPicture, showPicture, subTitle,canAddCart) VALUES '
        sub_str = get_commodity(all_commodity)

        with open(name2, 'w', encoding='utf-8') as sql_f:
            sql_f.write(sql+'\n'+sub_str)

if __name__ == '__main__':
    changeSQl('egg.json','egg.sql')