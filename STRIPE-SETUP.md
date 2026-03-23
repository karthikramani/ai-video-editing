# Stripe Setup for AI Video Editing Masterclass

## Product Details

**Product Name:** AI Video Editing Masterclass  
**Price:** $297 USD (one-time)  
**Payment Plan:** 3 payments of $99 USD

## Steps to Set Up

1. **Go to Stripe Dashboard:** https://dashboard.stripe.com/products

2. **Create Product:**
   - Name: `AI Video Editing Masterclass`
   - Description: `Complete training system to cut video editing time by 70% using AI tools`
   - Image: Upload thumbnail (optional)

3. **Add Pricing:**
   - **Option 1 (One-time):**
     - Price: $297 USD
     - Billing: One-time
     - Name: "Full Payment"
   
   - **Option 2 (Payment Plan):**
     - Price: $99 USD  
     - Billing: Recurring (3 installments)
     - Name: "3-Payment Plan"
     - Cancel after 3 payments

4. **Create Checkout Session:**
   - Use Stripe Checkout
   - Success URL: `https://ai-video-editing-psi.vercel.app/thank-you`
   - Cancel URL: `https://ai-video-editing-psi.vercel.app`

5. **Get Payment Link:**
   - Copy the Stripe payment link
   - Update the CTA buttons in index.html to point to this link

## What's Needed

To complete Stripe integration, provide:
- Stripe Secret Key (sk_live_...)
- Stripe Publishable Key (pk_live_...)

Save to: `credentials/stripe-keys.txt`

## Current Status

⏳ **Pending:** Stripe product creation (requires manual setup or API keys)

Once Stripe product is created:
1. Update CTA button href in index.html
2. Test checkout flow
3. Verify success/cancel redirects work
