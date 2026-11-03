# Task 1 – Conditions and Strings

## 1. Code Analysis

**السطر الأول: clean.lower()**

* التوقع: [sara.ahmed@tfco.sa](mailto:sara.ahmed@tfco.sa)
* الناتج الفعلي: [sara.ahmed@tfco.sa](mailto:sara.ahmed@tfco.sa)
* السبب: تحويل جميع الحروف إلى صغيرة.

**السطر الثاني: email.count("a"), clean.lower().count("a")**

* التوقع: 2, 4
* الناتج الفعلي: 2, 4
* السبب: العد يراعي حالة الأحرف الكبيرة والصغيرة.

**السطر الثالث: "tfco" in email, "tfco" in clean.lower()**

* التوقع: False, True
* الناتج الفعلي: False, True
* السبب: البحث حساس لحالة الأحرف.

**السطر الرابع: clean.startswith("sara")**

* التوقع: False
* الناتج الفعلي: False
* السبب: النص يبدأ بحرف S كبير.

**السطر الخامس: len(email), len(clean)**

* التوقع: 21, 18
* الناتج الفعلي: 21, 18
* السبب: حذف المسافات من الأطراف يقلل طول النص.

**السطر السادس: clean[:4], clean[-2:]**

* التوقع: Sara, SA
* الناتج الفعلي: Sara, SA
* السبب: استخراج أول أربعة أحرف وآخر حرفين.

## 2. Elif Conditions

الكود بعد التصحيح:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
```

السبب: شرط Pass كان يُفحص أولاً، لذلك لم يصل البرنامج إلى شرط Excellent.

القاعدة العامة: ترتيب الشروط يكون من الأعلى إلى الأقل، حتى لا يتحقق شرط عام قبل شرط أكثر تحديدًا.

## 3. Boolean Expressions

```python
x = 7

print(x > 3 and x % 2 == 0)
# False

print(not (x < 2) or x == 6)
# True

print(x * 2 >= 7 and not x == 5)
# True
```

النواتج بالترتيب:

1. False
2. True
3. True

## 4. Login System

نستخدم strip() لحذف المسافات الزائدة من أطراف اسم المستخدم، وlower() لتوحيد الحروف وتسهيل المقارنة.

لا نستخدم lower() مع كلمة المرور لأن كلمات المرور حساسة لحالة الأحرف، وتغييرها قد يؤثر على التحقق من صحتها وأمان تسجيل الدخول.