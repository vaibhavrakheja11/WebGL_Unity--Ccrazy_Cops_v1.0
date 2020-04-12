using System;
using UnityEngine;
using System.Collections;
using UnityStandardAssets.CrossPlatformInput;

namespace UnityStandardAssets.Vehicles.Car
{
    [RequireComponent(typeof (CarController))]
    public class CarUserControl : MonoBehaviour
    {
        private CarController m_Car; // the car controller we want to use
        
        public GameObject car;
        public GameObject particleGameObjectL;
        public GameObject particleGameObjectR;
        public AudioClip[] PoliceAudioDialogs;
        

        public bool isReady;
        private float waitTime;

        public DialogueTrigger dialogueTrigger;
        public DialogueManager dialogueManager;

        public int dialogueNumber = 1;
        public AudioSource audioSource;

        private void Awake()
        {
            // get the car controller
            m_Car = GetComponent<CarController>();
            //Application.OpenURL("http://unity3d.com/");
            Application.ExternalEval("window.open('http://github.com');");
            isReady = true;
            waitTime = 3;
            
           
        }
        private void Start()
        {
            audioSource = GetComponent<AudioSource>();
        }

        

        private void FixedUpdate()
        {
            // pass the input to the car!
            float h = CrossPlatformInputManager.GetAxis("Horizontal");
            float v = CrossPlatformInputManager.GetAxis("Vertical");
#if !MOBILE_INPUT
            float handbrake = CrossPlatformInputManager.GetAxis("Jump");
            m_Car.Move(h, v, v, handbrake);
#else
            m_Car.Move(h, v, v, 0f);
#endif

        
        }

        private void Update()
        {
            float h = CrossPlatformInputManager.GetAxis("Horizontal");
            float v = CrossPlatformInputManager.GetAxis("Vertical");
            float handbrake = CrossPlatformInputManager.GetAxis("Jump");
            if(Input.GetKeyDown(KeyCode.LeftShift) && isReady){
                 Nitrous();
            }

            if(isReady)
            {
                particleGameObjectL.GetComponent<ParticleSystem>().Stop();
                particleGameObjectR.GetComponent<ParticleSystem>().Stop();
            }

            
             if(Input.GetKeyDown(KeyCode.Q))
             {
                    dialogueTrigger.TriggerDialogue();
             }

            if(Input.GetKeyDown(KeyCode.R))
            {
                dialogueManager.DisplayNextSentence(dialogueNumber);
                dialogueNumber++;
            }

        }

 
    public void Nitrous() {
            //audio.PlayOneShot(activateSound, 1);
            isReady = false;
            this.gameObject.GetComponent<Rigidbody>().AddForce(transform.forward * 500, ForceMode.Acceleration);
            particleGameObjectL.GetComponent<ParticleSystem>().Play();
            particleGameObjectR.GetComponent<ParticleSystem>().Play();
            StartCoroutine(Boost());
     
        }

        private void OnTriggerEnter(Collider other)
            {

                Debug.Log(other.gameObject.name);
                if( other.gameObject.name == "5")
                    {
                        dialogueManager.DisplayNextSentence(5);
                    }

                if( other.gameObject.name == "4")
                    {
                        dialogueManager.DisplayNextSentence(6);
                    }
                if( other.gameObject.name == "2")
                    {
                        dialogueManager.DisplayNextSentence(4);
                    }
                if( other.gameObject.name == "Stunt1")
                    {
                        dialogueManager.DisplayNextSentence(8);
                    }
                    
                if( other.gameObject.name == "GoldenGateBridge")
                    {
                        dialogueManager.DisplayNextSentence(9);
                    }
                if( other.gameObject.name == "GoldenGateBridge")
                    {
                        dialogueManager.DisplayNextSentence(9);
                    }
            }

            private void OnTriggerStay(Collider other)
            {

                
                if(Input.GetKeyDown(KeyCode.E) && other.gameObject.name == "5")
                    {
                    Application.ExternalEval("window.open('http://Github.com');"); 
                    audioSource.clip = PoliceAudioDialogs[4];
                    audioSource.Play();            
                    }
                if(Input.GetKeyDown(KeyCode.E) && other.gameObject.name == "4")
                    {
                    Application.ExternalEval("window.open('http://Github.com');"); 
                    audioSource.clip = PoliceAudioDialogs[1];
                    audioSource.Play();      
                    }
            }



        IEnumerator Boost()
            {
                yield return new WaitForSeconds(2.0f);
                isReady = true;
            }
    }
}
