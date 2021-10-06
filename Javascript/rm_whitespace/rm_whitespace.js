/**
 * @author Subham Das
 * @param String
 * @returns String without extra whitespaces.
 */

function removeExtraWhiteSpce(sentence) {
    // return sentence.replace(/\s+/g, " ").trim();

    let _splited = sentence.split(" ");
    const wordList = _splited.filter((e) => e.length > 0);
    let str = wordList.join(" ");
    return str;
}

removeExtraWhiteSpce("  Hello  JavaScript  ");
// returns "Hello JavaScript"
