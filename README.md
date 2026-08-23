# مجموعة عرابي المحاسبية — موقع المكتب

موقع ثابت (HTML/CSS/JS من غير build tools) لمكتب د. تامر عرابي، محاسب قانوني وخبير اقتصادي — عين شمس، القاهرة.

## الملفات

| الملف | الدور |
|---|---|
| `index.html` | الصفحة العربية (RTL) — دي الصفحة الرئيسية |
| `en/index.html` | الصفحة الإنجليزية (LTR) |
| `assets/style.css` | ستايل مشترك للصفحتين، مبني بـ CSS logical properties فبيشتغل RTL وLTR من نفس الكود |
| `assets/app.js` | الهيدر، قائمة الموبايل، الروابط الخارجية، وإظهار الأقسام مع السكرول |
| `privacy.html` / `en/privacy.html` | صفحتا سياسة الخصوصية بالعربية والإنجليزية |
| `build-preview.py` | بيبني `preview.html`: ملف واحد مكتفي بذاته فيه اللغتين والخطوط مدمجة — للمعاينة والمشاركة فقط |
| `fonts-inline.css` | خطوط Amiri وIBM Plex Sans Arabic كـ base64، بيستخدمها سكريبت المعاينة بس |
| `robots.txt` / `sitemap.xml` | جاهزين، محتاجين تعديل الدومين |

## التشغيل محليًا

```
python -m http.server 8000
```
وافتح `http://localhost:8000`.

## بناء ملف المعاينة

```
python build-preview.py
```

## قبل الرفع

1. غيّر `eng-mohamed-elsayedahmed.github.io/orabi-accounting` للدومين الحقيقي في: `index.html`، `en/index.html`، `sitemap.xml`، `robots.txt`.
2. حط صورة `assets/tamer-orabi.jpg` وفعّل وسم `<img>` المعلّق في قسم `#about` في الصفحتين.
3. اللوجو المستخدم في الهيدر هو `assets/media/orabi-logo-transparent.png` مع نسخة WebP أخف، بالإضافة إلى نسخ `orabi-logo-final.png` و`orabi-logo-final.jpg` للاستخدامات المختلفة.
4. فعّل سطور القيد والمعهد المعلّقة في `.creds` بعد التأكد من البيانات.

## الملكية والهوية

- التصميم والتطوير: **Mohamed Elsayed** — [Portfolio](https://eng-mohamed-elsayedahmed.github.io/portfolio/).

- **الخطوط:** Amiri للعناوين (مبني على حروف المطبعة الأميرية ببولاق) + IBM Plex Sans Arabic للنص.
- **الألوان:** كحلي وأزرق وذهبي، متوافقة مع شعار مجموعة عرابي المحاسبية.
- **العنصر المميز:** علامة النسر والكرة الأرضية المستخدمة في الشعار والـ Open Graph.
- **الأرشيف الإعلامي:** ٢٠ رابطًا فريدًا من يوتيوب وفيسبوك مع صور اللقاءات المرفقة من العميل.
- الموقع بيدعم الوضع الفاتح والداكن تلقائيًا، و`prefers-reduced-motion`.
