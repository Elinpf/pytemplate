## 简介

本工具用于将数据和逻辑分离，使用excel存储数据。

## 安装方法

```
python setup.py install
```

## EXCEL格式

excel中第一行是要替换的占位符，第二行是备注，后面每行为一组进行替换。(文件`data.xlsx`作为参考)

## 使用示例

如果所使用的数据不需要进行二次计算，则可以使用以下方式

```py
import pytemplate

data_file = 'data.xlsx'
template_file = 'template.txt'

g = pytemplate.ExcelDataGenerator()
g.load(data_file)

template_str = pytemplate.load_template(template_file)
for ds, info in g.data:
    pytemplate.write(template_str, '{}.txt'.format(ds), info)
```

如果所使用的数据需要进行二次计算，或者需要新增，则可以使用以下方法

```py
import pytemplate

data_file = 'data.xlsx'
template_file = 'template.txt'

g = pytemplate.ExcelDataGenerator()
for ds in g.load_generator(data_file):
    # 本地bgp宣告的网段掩码， 通过acl的反掩码得到
    ds['local_bgp_network_mask'] = pytemplate.wildcard_mask_to_netmask(
        ds['local_acl_wildcard_mask'])
    # 本地bgp宣告网段的掩码长度
    ds['local_bgp_network_prefix'] = pytemplate.netmask_to_bit_length(
        ds['local_bgp_network_mask'])
    # 增加IP，得到对端IP地址
    ds['peer_ip'] = pytemplate.add_ip_address(ds['local_ip'], 1)


for ds, info in g.data:
    pytemplate.write(template_str, '{}.txt'.format(ds), info)