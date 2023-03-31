let _s = {} // oneliner snippets
const shuffle = array => array.sort(() => Math.random() - 0.5)
_s.shfl = shuffle
const incrementNumbers = (start, step, total) => Array.from({ length: total }, (_, i) => start + i * step)
_s.incNums = incrementNumbers
const getShuffled = (start, step, total) => _s.shfl(_s.incNums(start, step, total))
_s.g_shfl = getShuffled

const allEqual = arr => arr.every( v => v === arr[0] )

module.exports = {
    shuffle,
    incrementNumbers,
    getShuffled,
    _s
}
