import Head from 'next/head'
import { Box } from '../components/box'
import { Output } from '../components/output'
import {
  TabsContent,
  TabsRoot,
  TabsList,
  TabsTrigger
} from '../components/tabs'
import { VideoForm } from '../components/video-form'
import { styled } from '../stitches.config'

const Text = styled('p', {
  fontFamily: '$system',
  color: '$hiContrast'
})

const Container = styled('div', {
  display: 'flex',
  flexDirection: 'column',
  // flexWrap: 'nowrap',
  height: '100vh',
  marginY: 0,
  marginX: 'auto',
  paddingX: '$3',
  paddingY: 0,

  variants: {
    size: {
      1: {
        maxWidth: '300px'
      },
      2: {
        maxWidth: '585px'
      },
      3: {
        maxWidth: '865px'
      }
    }
  }
})

export default function Home() {
  return (
    <Box css={{ paddingY: '$6' }}>
      <Head>
        <title>Youtube Transcription &amp; Japanese Translation</title>
      </Head>
      <Container size={{ '@initial': '1', '@bp1': '2' }}>
        <Text as="h1">Youtube Transcription &amp; Japanese Translation</Text>
        <VideoForm />
        <TabsRoot defaultValue="progress">
          <TabsList aria-label="Output">
            <TabsTrigger value="progress">Progress</TabsTrigger>
            <TabsTrigger value="result">Result</TabsTrigger>
          </TabsList>
          <TabsContent value="progress">
            <Output>{'Progress will go here '.repeat(100)}</Output>
          </TabsContent>
          <TabsContent value="result">
            <Output>{'Result will go here '.repeat(10)}</Output>
          </TabsContent>
        </TabsRoot>
      </Container>
    </Box>
  )
}
