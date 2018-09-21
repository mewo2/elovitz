# Elovitz: rule-based English pronunciation

This is code which implements a rule-based system for determining the pronunciation of English words. It's based on the algorithm described in [this 1976 paper by Elovitz et al.](http://www.dtic.mil/get-tr-doc/pdf?AD=ADA021929)

Example usage:
```
>>> import elovitz
>>> elovitz.pronounce('unique')
['y', 'uw', 'n', 'iy', 'k']
>>> elovitz.ipa('unique')
'juːniːk'
```

## Support, licensing, ongoing development

This is code I wrote for [a specific project](http://newborderballads.com/), which I have now finished.

The code is available under the [MIT license](LICENSE.md), so you can fork it,
improve it, learn from it, build upon it. However, I have no interest in
maintaining it as an ongoing open source project, nor in providing support for
it. Pull requests will probably be either ignored or closed.

If you do make something interesting with this code, please do still let me know! I'm sorry that I can't provide any support, but I am still genuinely interested in seeing creative applications of the code.