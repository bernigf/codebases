// Applying your knowledge of concurrency, complete the following exercise.
// An array with N random numbers must be generated,
// each of these numbers must be sent through a go routine to a channel. (one go routine per element)
// On the other hand, an independent process must be receiving these transmitted numbers and storing the even and odd numbers in different slices,
// at the end it must print both slices with the values received

// improvement.
// instead of storing the even and odd values ​​in different slices,
// they should be transmitted to a different channel and this should be received by a different process that will print the values

package main

import (
	"fmt"
	"math"
	"math/rand/v2"
	"time"
)

// producer generates random numbers and sends them on ch.
// It closes ch when done so the consumer can terminate its range loop.
func producer(ch chan int) {
	N := 10 // number of random values to produce
	for i := 0; i < N; i++ {
		num := rand.IntN(100)
		fmt.Println("Producer: sending", num)
		ch <- num // send the random number through the channel
	}
	fmt.Println("Producer: Finished sending")
	close(ch)
}

// consumer reads values from ch, classifies them as even or odd, and prints them.
// When ch is closed and all values are consumed, it closes done to signal completion.
func consumer(ch <-chan int, done chan<- struct{}) {
	for i := range ch { // receive the numbers from the channel
		time.Sleep(time.Second)
		fmt.Println("Consumer: receiving", i)
		if math.Mod(float64(i), 2.0) == 0 { // even
			fmt.Println("Consumer -> Stored in evens:", i)
		} else { // odd
			fmt.Println("Consumer -> Stored in odds:", i)
		}
	}
	fmt.Println("Consumer: Finished consuming all numbers -> Signaling completion closing the done channel")
	close(done)
}


func main() {

	// Create an unbuffered channel of type int.
	// This channel will be used to send the generated random numbers
	// from the producer goroutine to the consumer goroutine, one at a time.
	// The unbuffered nature means sends/receives will block until both sides are ready,
	// thereby synchronizing the producer and consumer.
	ch := make(chan int)           

	// Create an unbuffered channel of empty structs.
	// This is used solely for signaling completion (synchronization) between goroutines.
	// The consumer will close this channel when it has finished processing all received numbers.
	// The empty struct type struct{} doesn't consume memory, making it ideal for signaling.
	done := make(chan struct{})    

	// Start the producer goroutine.
	// This will generate random numbers and send them through the channel.
	go producer(ch)

	// Start the consumer goroutine.
	// This will receive the numbers from the channel, classify them as even or odd,
	// and print them. It will also signal completion by closing the done channel.
	// Second parameter is the done channel, which is used to signal completion.
	go consumer(ch, done)

	// Next line will block the main goroutine until the consumer signals completion by closing the done channel.
	// This ensures the main function waits for the consumer to finish processing before exiting.
	// This line blocks the main goroutine until the 'done' channel is closed by the consumer.	
	
	// The syntax '<-done' is a receive operation from a channel.
	// In Go, '<-channel' means "wait until a value is available from channel, then receive it." 
	// If no value is ever sent, or if the channel is just closed, then the receive unblocks upon close.
	// 
	// In this context, 'done' is a channel of empty structs (struct{}), and our code
	// doesn't actually care *what* comes from the channel—just that the channel
	// was closed (which signals completion). So:
	//   <-done
	// is a receive from 'done', and it blocks until either:
	//   - A value is sent to 'done' (which never happens here)
	//   - Or the 'done' channel is closed
	// 
	// When 'close(done)' is called in the consumer, <-done unblocks.
	// It's common to use this idiom for synchronization, where the "main" goroutine blocks
	// until another goroutine signals "done" by closing a channel.
	<-done

}
