const readline = require("readline-sync")
//const chalk = require("chalk")
//import chalk from "chalk"

const printIntro = (numDigits) => {
  const info = `Bages, a deductive logic game,
By Al Sweigart 

I am thinking of a ${numDigits}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico            One digit is correct but in the wrong position
    Fermi           One digit is correct but in the right position
    Bagels          No digit is correct
    
For example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico.`
  console.log(info)
}


let _s = {} // oneliner snippets
const shuffle = array => array.sort(() => Math.random() - 0.5)
_s.shfl = shuffle
const incrementNumbers = (start, step, total) => Array.from({ length: total }, (_, i) => start + i * step)
_s.incNums = incrementNumbers
const getShuffled = (start, step, total) => _s.shfl(_s.incNums(start, step, total))
_s.g_shfl = getShuffled

/*
const getShuffled = () => {
  let counter = 0
  return Array.from(Array(10), () => counter++)
    .map((value) => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value)
}
*/
//console.log(getShuffled())

const getSecretNum = numDigits => getShuffled(0, 1, 10).splice(0, numDigits).join("")
//console.log(getSecretNum(3))

const isValidNumInput = (input, numInputs) => !isNaN(+input) && +input.length === numInputs 

const rf_getInputGuess = (guess, numGuesses, numDigits) => {
  while (isValidNumInput(guess, numDigits)) 
    guess = readline.question(`Guess #${numGuesses}: `)
  return guess
} 

const getInputGuess = (numGuesses, numDigits) => {
  let guess
  while (!isValidNumInput(guess, numDigits)) 
    //isNaN(guess) ||
    //\!Number.isInteger(+guess) ||
    //+guess.length != numDigits
  {
    guess = readline.question(`Guess #${numGuesses}: `)
  }
  return guess
}
//console.log(getInputGuess(1, 3))

const getClues = (guess, secretNum) => {
  if (guess == secretNum) return "You got it!"

  clues = []
  for (const index in guess) {
    if (guess.charAt(index) == secretNum.charAt(index)) clues.push("Fermi")
    else if (secretNum.indexOf(guess.charAt(index)) != -1) clues.push("Pico")
  }

  return clues.length ? clues.sort().join(" ") : "Bagels"
}

const main = () => {
  const NUM_DIGITS = 3
  const MAX_GUESSES = 10

  const THOUGHT_UP_MSG = "I have thought up a number."
  const MAX_GUESSES_MSG = `You have ${MAX_GUESSES} guesses to get it.`

  printIntro(NUM_DIGITS)

  while (true) {
    const secretNum = getSecretNum(NUM_DIGITS)
    console.log(THOUGHT_UP_MSG)
    console.log(MAX_GUESSES_MSG)

    let numGuesses = 1
    let guess, clues
    while (numGuesses <= MAX_GUESSES) {
      guess = getInputGuess(numGuesses, NUM_DIGITS)
      clues = getClues(guess, secretNum)
      console.log(clues)
      numGuesses++

      if (guess == secretNum) break
      if (numGuesses > MAX_GUESSES) {
        console.log("You run out of guesses.")
        console.log(`The answer was ${secretNum}.`)
      }
    }
    answer = readline.question(`Do you want to play again? (yes or now)`)
    if (!answer.toLowerCase().startsWith("y")) break
  }
  console.log("Thank's for playing!")
}

main()