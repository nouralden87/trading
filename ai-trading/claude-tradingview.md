# 🤖 Claude + TradingView — AI Trading Setup

**Source:** [GitHub Open Source Project](https://github.com) | [@girsta Instagram](https://www.instagram.com/reel/DZzdYr0tg8D/)

---

## الفكرة

ربط **Claude Code** (أو أي وكيل AI) بـ **TradingView Desktop** عبر **Chrome DevTools Protocol (CDP)** ليتحكم الـ AI مباشرة في منصة التداول.

---

## المكونات

```
Claude Code / AI Agent
       ↓ (MCP / CDP)
TradingView Desktop App
       ↓
Chrome DevTools Protocol
       ↓
القدرات:
  • قراءة الشارتات
  • تغيير الرموز (symbols)
  • تغيير الأطر الزمنية (timeframes)
  • كتابة Pine Script
  • تشغيل replay mode
  • إدارة التنبيهات (alerts)
  • التقاط screenshots
  • الرسم على الشارت
  • حفظ وتحميل تخطيطات الشارت
```

---

## إعداد البيئة

```bash
# 1. تشغيل TradingView Desktop مع debugging port
tradingview --remote-debugging-port=9222

# 2. إعداد MCP Server (Claude Code)
# في .mcp.json:
{
  "mcpServers": {
    "tradingview": {
      "command": "node",
      "args": ["path/to/tradingview-mcp-server.js"],
      "env": {
        "CDP_PORT": "9222"
      }
    }
  }
}

# 3. اختبار الاتصال
# داخل Claude Code:
# > Read the current chart
# > Change symbol to BTCUSDT
# > Write a Pine Script strategy
```

---

## قدرات الـ AI Agent

- **قراءة السوق:** تحليل الشارت الحالي، المؤشرات، البيانات
- **كتابة استراتيجيات:** توليد Pine Script وتجربته مباشرة
- **Backtesting:** اختبار الاستراتيجية على بيانات تاريخية
- **تنبيهات:** إعداد تنبيهات تلقائية للأسعار
- **رسم:** إضافة خطوط دعم/مقاومة، فيبوناتشي
- **مراقبة:** متابعة عدة أزواج في نفس الوقت

---

## ⚠️ قيود

- غير مرتبط رسمياً بـ TradingView
- يعتمد على واجهات داخلية غير موثقة
- قد ينكسر مع تحديثات TradingView
- ليس بديلاً عن استراتيجية تداول حقيقية

---

## 🔗 مشاريع مشابهة

- **MCP Servers:** [mcpservers.org](https://mcpservers.org)
- **TradingView MCP:** ابحث في GitHub عن `tradingview-mcp`
- **Freqtrade:** [freqtrade.io](https://www.freqtrade.io) — بوت تداول مفتوح المصدر
- **Jesse:** [jesse.trade](https://jesse.trade) — إطار عمل تداول آلي
