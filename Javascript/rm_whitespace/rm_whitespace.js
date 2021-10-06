/**
 * @author Subham Das
 * @param String
 * @returns String without extra whitespaces.
 */

function removeExtraWhiteSpce(sentence) {
    return sentence.replace(/\s+/g, " ").trim();
}

removeExtraWhiteSpce("  Hello  JavaScript  ");
// returns "Hello JavaScript"
