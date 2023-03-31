const readline = require("readline-sync")

const bitmap = `
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................`
const lines = bitmap.split('\n')

console.log('Bitmap message. By Al Sweigart...')
console.log('Enter the message to display with bitmap.')
answer = readline.question('> ')

if (!answer.length) process.exit(1)

let bit = ''
for (const line of lines.values()) {
    let message = ''
    for (const index in line) {
        bit = line.charAt(index)
        message += !!bit.trim()
            ? answer[index % answer.length]
            : ' '
    }
    console.log(message)
}

