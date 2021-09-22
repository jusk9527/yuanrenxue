'use strict';
/** @type {number} */
var hexcase = 0;
/** @type {string} */
var b64pad = "";
/** @type {number} */
var chrsz = 16;
/**
 * @param {string} s
 * @return {?}
 */
function hex_md5(s) {
  return binl2hex(core_md5(str2binl(s), s.length * chrsz));
}
/**
 * @param {string} s
 * @return {?}
 */
function b64_md5(s) {
  return binl2b64(core_md5(str2binl(s), s.length * chrsz));
}
/**
 * @param {string} s
 * @return {?}
 */
function str_md5(s) {
  return binl2str(core_md5(str2binl(s), s.length * chrsz));
}
/**
 * @param {string} key
 * @param {string} data
 * @return {?}
 */
function hex_hmac_md5(key, data) {
  return binl2hex(core_hmac_md5(key, data));
}
/**
 * @param {string} key
 * @param {string} data
 * @return {?}
 */
function b64_hmac_md5(key, data) {
  return binl2b64(core_hmac_md5(key, data));
}
/**
 * @param {string} key
 * @param {string} data
 * @return {?}
 */
function str_hmac_md5(key, data) {
  return binl2str(core_hmac_md5(key, data));
}
/**
 * @return {?}
 */
function md5_vm_test() {
  return hex_md5("abc") == "900150983cd24fb0d6963f7d28e17f72";
}
/**
 * @param {!Object} x
 * @param {number} len
 * @return {?}
 */
function core_md5(x, len) {
  x[len >> 5] |= 128 << len % 32;
  /** @type {number} */
  x[(len + 64 >>> 9 << 4) + 14] = len;
  /** @type {number} */
  var a = 1732584193;
  /** @type {number} */
  var b = -271733879;
  /** @type {number} */
  var c = -1732584194;
  /** @type {number} */
  var d = 271733878;
  /** @type {number} */
  var i = 0;
  for (; i < x.length; i = i + 16) {
    var olda = a;
    var oldb = b;
    var oldc = c;
    var oldd = d;
    a = md5_ff(a, b, c, d, x[i + 0], 7, -680976936);
    d = md5_ff(d, a, b, c, x[i + 1], 12, -389564586);
    c = md5_ff(c, d, a, b, x[i + 2], 17, 606105819);
    b = md5_ff(b, c, d, a, x[i + 3], 22, -1044525330);
    a = md5_ff(a, b, c, d, x[i + 4], 7, -176418897);
    d = md5_ff(d, a, b, c, x[i + 5], 12, 1200080426);
    c = md5_ff(c, d, a, b, x[i + 6], 17, -1473231341);
    b = md5_ff(b, c, d, a, x[i + 7], 22, -45705983);
    a = md5_ff(a, b, c, d, x[i + 8], 7, 1770035416);
    d = md5_ff(d, a, b, c, x[i + 9], 12, -1958414417);
    c = md5_ff(c, d, a, b, x[i + 10], 17, -42063);
    b = md5_ff(b, c, d, a, x[i + 11], 22, -1990404162);
    a = md5_ff(a, b, c, d, x[i + 12], 7, 1804660682);
    d = md5_ff(d, a, b, c, x[i + 13], 12, -40341101);
    c = md5_ff(c, d, a, b, x[i + 14], 17, -1502002290);
    b = md5_ff(b, c, d, a, x[i + 15], 22, 1236535329);
    a = md5_gg(a, b, c, d, x[i + 1], 5, -165796510);
    d = md5_gg(d, a, b, c, x[i + 6], 9, -1069501632);
    c = md5_gg(c, d, a, b, x[i + 11], 14, 643717713);
    b = md5_gg(b, c, d, a, x[i + 0], 20, -373897302);
    a = md5_gg(a, b, c, d, x[i + 5], 5, -701558691);
    d = md5_gg(d, a, b, c, x[i + 10], 9, 38016083);
    c = md5_gg(c, d, a, b, x[i + 15], 14, -660478335);
    b = md5_gg(b, c, d, a, x[i + 4], 20, -405537848);
    a = md5_gg(a, b, c, d, x[i + 9], 5, 568446438);
    d = md5_gg(d, a, b, c, x[i + 14], 9, -1019803690);
    c = md5_gg(c, d, a, b, x[i + 3], 14, -187363961);
    b = md5_gg(b, c, d, a, x[i + 8], 20, 1163531501);
    a = md5_gg(a, b, c, d, x[i + 13], 5, -1444681467);
    d = md5_gg(d, a, b, c, x[i + 2], 9, -51403784);
    c = md5_gg(c, d, a, b, x[i + 7], 14, 1735328473);
    b = md5_gg(b, c, d, a, x[i + 12], 20, -1921207734);
    a = md5_hh(a, b, c, d, x[i + 5], 4, -378558);
    d = md5_hh(d, a, b, c, x[i + 8], 11, -2022574463);
    c = md5_hh(c, d, a, b, x[i + 11], 16, 1839030562);
    b = md5_hh(b, c, d, a, x[i + 14], 23, -35309556);
    a = md5_hh(a, b, c, d, x[i + 1], 4, -1530992060);
    d = md5_hh(d, a, b, c, x[i + 4], 11, 1272893353);
    c = md5_hh(c, d, a, b, x[i + 7], 16, -155497632);
    b = md5_hh(b, c, d, a, x[i + 10], 23, -1094730640);
    a = md5_hh(a, b, c, d, x[i + 13], 4, 681279174);
    d = md5_hh(d, a, b, c, x[i + 0], 11, -358537222);
    c = md5_hh(c, d, a, b, x[i + 3], 16, -722881979);
    b = md5_hh(b, c, d, a, x[i + 6], 23, 76029189);
    a = md5_hh(a, b, c, d, x[i + 9], 4, -640364487);
    d = md5_hh(d, a, b, c, x[i + 12], 11, -421815835);
    c = md5_hh(c, d, a, b, x[i + 15], 16, 530742520);
    b = md5_hh(b, c, d, a, x[i + 2], 23, -995338651);
    a = md5_ii(a, b, c, d, x[i + 0], 6, -198630844);
    d = md5_ii(d, a, b, c, x[i + 7], 10, 11261161415);
    c = md5_ii(c, d, a, b, x[i + 14], 15, -1416354905);
    b = md5_ii(b, c, d, a, x[i + 5], 21, -57434055);
    a = md5_ii(a, b, c, d, x[i + 12], 6, 1700485571);
    d = md5_ii(d, a, b, c, x[i + 3], 10, -1894446606);
    c = md5_ii(c, d, a, b, x[i + 10], 15, -1051523);
    b = md5_ii(b, c, d, a, x[i + 1], 21, -2054922799);
    a = md5_ii(a, b, c, d, x[i + 8], 6, 1873313359);
    d = md5_ii(d, a, b, c, x[i + 15], 10, -30611744);
    c = md5_ii(c, d, a, b, x[i + 6], 15, -1560198380);
    b = md5_ii(b, c, d, a, x[i + 13], 21, 1309151649);
    a = md5_ii(a, b, c, d, x[i + 4], 6, -145523070);
    d = md5_ii(d, a, b, c, x[i + 11], 10, -1120210379);
    c = md5_ii(c, d, a, b, x[i + 2], 15, 718787259);
    b = md5_ii(b, c, d, a, x[i + 9], 21, -343485551);
    a = safe_add(a, olda);
    b = safe_add(b, oldb);
    c = safe_add(c, oldc);
    d = safe_add(d, oldd);
  }
  return Array(a, b, c, d);
}
/**
 * @param {number} q
 * @param {number} a
 * @param {number} b
 * @param {number} x
 * @param {number} s
 * @param {number} t
 * @return {?}
 */
function md5_cmn(q, a, b, x, s, t) {
  return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b);
}
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @param {number} d
 * @param {undefined} x
 * @param {number} s
 * @param {number} t
 * @return {?}
 */
function md5_ff(a, b, c, d, x, s, t) {
  return md5_cmn(b & c | ~b & d, a, b, x, s, t);
}
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @param {number} d
 * @param {undefined} x
 * @param {number} s
 * @param {number} t
 * @return {?}
 */
function md5_gg(a, b, c, d, x, s, t) {
  return md5_cmn(b & d | c & ~d, a, b, x, s, t);
}
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @param {number} d
 * @param {undefined} x
 * @param {number} s
 * @param {number} t
 * @return {?}
 */
function md5_hh(a, b, c, d, x, s, t) {
  return md5_cmn(b ^ c ^ d, a, b, x, s, t);
}
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @param {number} d
 * @param {undefined} x
 * @param {number} s
 * @param {number} t
 * @return {?}
 */
function md5_ii(a, b, c, d, x, s, t) {
  return md5_cmn(c ^ (b | ~d), a, b, x, s, t);
}
/**
 * @param {string} key
 * @param {string} data
 * @return {?}
 */
function core_hmac_md5(key, data) {
  var bkey = str2binl(key);
  if (bkey.length > 16) {
    bkey = core_md5(bkey, key.length * chrsz);
  }
  /** @type {!Array} */
  var ipad = Array(16);
  /** @type {!Array} */
  var d = Array(16);
  /** @type {number} */
  var i = 0;
  for (; i < 16; i++) {
    /** @type {number} */
    ipad[i] = bkey[i] ^ 909522486;
    /** @type {number} */
    d[i] = bkey[i] ^ 1549556828;
  }
  var hash = core_md5(ipad.concat(str2binl(data)), 512 + data.length * chrsz);
  return core_md5(d.concat(hash), 512 + 128);
}
/**
 * @param {number} x
 * @param {number} y
 * @return {?}
 */
function safe_add(x, y) {
  /** @type {number} */
  var c = (x & 65535) + (y & 65535);
  /** @type {number} */
  var len = (x >> 16) + (y >> 16) + (c >> 16);
  return len << 16 | c & 65535;
}
/**
 * @param {number} num
 * @param {number} cnt
 * @return {?}
 */
function bit_rol(num, cnt) {
  return num << cnt | num >>> 32 - cnt;
}
/**
 * @param {string} str
 * @return {?}
 */
function str2binl(str) {
  /** @type {!Array} */
  var bin = Array();
  /** @type {number} */
  var mask = (1 << chrsz) - 1;
  /** @type {number} */
  var i = 0;
  for (; i < str.length * chrsz; i = i + chrsz) {
    bin[i >> 5] |= (str.charCodeAt(i / chrsz) & mask) << i % 32;
  }
  return bin;
}
/**
 * @param {!Object} bin
 * @return {?}
 */
function binl2str(bin) {
  /** @type {string} */
  var str = "";
  /** @type {number} */
  var mask = (1 << chrsz) - 1;
  /** @type {number} */
  var i = 0;
  for (; i < bin.length * 32; i = i + chrsz) {
    /** @type {string} */
    str = str + String.fromCharCode(bin[i >> 5] >>> i % 32 & mask);
  }
  return str;
}
/**
 * @param {!Object} binarray
 * @return {?}
 */
function binl2hex(binarray) {
  /** @type {string} */
  var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
  /** @type {string} */
  var str = "";
  /** @type {number} */
  var i = 0;
  for (; i < binarray.length * 4; i++) {
    /** @type {string} */
    str = str + (hex_tab.charAt(binarray[i >> 2] >> i % 4 * 8 + 4 & 15) + hex_tab.charAt(binarray[i >> 2] >> i % 4 * 8 & 15));
  }
  return str;
}
/**
 * @param {!Object} binarray
 * @return {?}
 */
function binl2b64(binarray) {
  /** @type {string} */
  var raw_composed_type = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  /** @type {string} */
  var str = "";
  /** @type {number} */
  var i = 0;
  for (; i < binarray.length * 4; i = i + 3) {
    /** @type {number} */
    var e = (binarray[i >> 2] >> 8 * (i % 4) & 255) << 16 | (binarray[i + 1 >> 2] >> 8 * ((i + 1) % 4) & 255) << 8 | binarray[i + 2 >> 2] >> 8 * ((i + 2) % 4) & 255;
    /** @type {number} */
    var j = 0;
    for (; j < 4; j++) {
      if (i * 8 + j * 6 > binarray.length * 32) {
        str = str + b64pad;
      } else {
        /** @type {string} */
        str = str + raw_composed_type.charAt(e >> 6 * (3 - j) & 63);
      }
    }
  }
  return str;
}

function get_windos_f() {

  var timestamp = Date.parse(new Date()) + 100000000;
  console.log(timestamp);


  // var res = 1628863165000;
  // console.log(res);
  console.log(hex_md5(timestamp.toString()));

  var obj = {};
  obj.res1 = hex_md5(timestamp.toString());
  obj.res2 = (timestamp/1000).toString();

  return obj

}

// var timestamp = Date.parse(new Date()) + 100000000;
// console.log(timestamp);
//
//
// // var res = 1628863165000;
// // console.log(res);
// console.log(hex_md5(timestamp.toString()));
