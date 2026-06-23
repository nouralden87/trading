# 📊 استراتيجيات التداول

---

## 1. 🟢 المتوسطات المتحركة (MA Crossover)

**الإشارة:** تقاطع MA سريع مع MA بطيء

```python
# Pine Script
fast_ma = ta.sma(close, 9)
slow_ma = ta.sma(close, 21)

if ta.crossover(fast_ma, slow_ma):
    strategy.entry("Long", strategy.long)
if ta.crossunder(fast_ma, slow_ma):
    strategy.close("Long")
```

---

## 2. 🟡 بولينجر باند (Bollinger Bands)

**الإشارة:** السعر يلامس الحد السفلي (شراء) أو العلوي (بيع)

```python
basis = ta.sma(close, 20)
dev = ta.stdev(close, 20)
upper = basis + 2 * dev
lower = basis - 2 * dev
```

---

## 3. 🔴 RSI (مؤشر القوة النسبية)

**الإشارة:** RSI < 30 = شراء (تشبع بيعي)، RSI > 70 = بيع (تشبع شرائي)

```python
rsi = ta.rsi(close, 14)
buy_signal = rsi < 30
sell_signal = rsi > 70
```

---

## 4. 🟣 MACD

**الإشارة:** تقاطع MACD مع Signal line

```python
[macd, signal, hist] = ta.macd(close, 12, 26, 9)
buy = ta.crossover(macd, signal)
sell = ta.crossunder(macd, signal)
```

---

## 5. 🟠 سكالبينج (Scalping)

- إطار زمني: 1m-5m
- هدف: 0.1%-0.5%
- وقف خسارة: ضيق جداً
- حجم كبير، أرباح صغيرة متكررة

---

## 6. 🔵 سوينغ (Swing Trading)

- إطار زمني: 4h-Daily
- هدف: 3%-10%
- الاحتفاظ: أيام إلى أسابيع
- يعتمد على الدعوم والمقاومات

---

## ⚠️ إدارة المخاطر

- **لا تخاطر بأكثر من 1-2% من رأس المال في الصفقة الواحدة**
- دائماً استخدم Stop Loss
- نسبة Risk/Reward لا تقل عن 1:2
