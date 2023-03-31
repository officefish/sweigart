function logCall() {
  const BASH_EXP = "\x1b["

  const RESET_ALL = 0
  const BOLD = 1
  const DIM = 2
  const UNDERLINED = 4

  const LIGHT_GREEN = 92

  const CALL_TAG = "[CALL] : "

  const RESET_EXP = `${BASH_EXP}${RESET_ALL}m`
  const CALL_EXP = `${BASH_EXP}${DIM};${LIGHT_GREEN}m${CALL_TAG}${RESET_EXP}`

  try {
    throw new Error("I am fake Error")
  } catch (e) {
    const functionName = e.stack.split("at")[2].split(" ")[1]
    const FUNC_EXP = `${BASH_EXP}${BOLD};${LIGHT_GREEN}m${functionName}${RESET_EXP}`
    const value = `${CALL_EXP}${FUNC_EXP}`
    console.log(value)
  }
}

function logStack() {
  try {
    throw new Error("I am fake Error")
  } catch (e) {
    const stack = []
    for (const value of e.stack
      .split('at')
      .slice(2)
      .values()) {
        if (value.includes('Object')) break 
        stack.push(value.split(' ')[1])
    }    
    for (const [index, value] of stack.reverse().entries()) 
      console.log (`${index} -> \x1b[92m${value}\x1b[0m`)
  }
}

module.exports = { logCall, logStack }
