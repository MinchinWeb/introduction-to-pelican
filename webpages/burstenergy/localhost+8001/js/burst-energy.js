/* Burst Energy website   burstenergy.ca
 * Copyright (c) 2014 Burst Energy
 *
 * Site specific CSS
 *
 * Site created by Wm Minchin
 * Last updated January 25, 2014
 */

/* For IE 10 in Win8 and Win Phone 8 */

if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
    var msViewportStyle = document.createElement("style")
    msViewportStyle.appendChild(
      document.createTextNode(
        "@-ms-viewport{width:auto!important}"
      )
    )
    document.getElementsByTagName("head")[0].appendChild(msViewportStyle)
}
